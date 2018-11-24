# Mpow Bluetooth Over-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 -4.0; 23 -4.3; 25 -4.6; 28 -4.9; 31 -5.0; 34 -5.1; 37 -5.1; 41 -5.0; 45 -5.1; 49 -5.2; 54 -5.4; 60 -5.8; 66 -6.2; 72 -6.5; 79 -6.8; 87 -7.3; 96 -7.8; 106 -8.4; 116 -8.8; 128 -9.2; 141 -9.4; 155 -9.6; 170 -9.6; 187 -9.5; 206 -9.3; 227 -8.9; 249 -8.4; 274 -7.7; 302 -7.2; 332 -6.6; 365 -4.9; 402 -2.9; 442 -1.2; 486 -0.6; 535 0.2; 588 1.2; 647 2.5; 712 3.4; 783 3.2; 861 1.8; 947 0.6; 1042 -0.4; 1146 -0.9; 1261 -0.9; 1387 -0.9; 1526 -1.0; 1678 -1.3; 1846 -1.7; 2031 -1.9; 2234 -1.6; 2457 -2.0; 2703 -2.7; 2973 -3.7; 3270 -4.5; 3597 -3.8; 3957 -1.2; 4353 0.8; 4788 3.4; 5267 2.7; 5793 5.1; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -1.4; 12418 -2.2; 13660 -2.2; 15026 -3.2; 16529 -0.7; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mpow Bluetooth Over-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mpow Bluetooth Over-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 44 Hz    | 0.37 | -4.9 dB |
| Peaking | 148 Hz   | 1.1  | -7.2 dB |
| Peaking | 266 Hz   | 2.07 | -5.3 dB |
| Peaking | 3174 Hz  | 2.09 | -4.9 dB |
| Peaking | 5826 Hz  | 2.6  | 6.1 dB  |
| Peaking | 343 Hz   | 5.94 | -2.1 dB |
| Peaking | 735 Hz   | 1.78 | 5.5 dB  |
| Peaking | 1060 Hz  | 0.96 | -2.0 dB |
| Peaking | 4724 Hz  | 8.88 | 2.1 dB  |
| Peaking | 14144 Hz | 1.58 | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Mpow%20Bluetooth%20Over-Ear/Mpow%20Bluetooth%20Over-Ear.png)