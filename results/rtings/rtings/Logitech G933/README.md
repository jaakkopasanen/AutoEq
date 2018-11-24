# Logitech G933

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.7dB
GraphicEQ: 21 -4.1; 23 -4.9; 25 -5.6; 28 -6.4; 31 -6.9; 34 -7.2; 37 -7.1; 41 -6.8; 45 -6.6; 49 -6.5; 54 -6.7; 60 -6.9; 66 -7.2; 72 -7.3; 79 -7.2; 87 -7.0; 96 -6.7; 106 -6.0; 116 -5.4; 128 -5.0; 141 -5.2; 155 -5.3; 170 -5.1; 187 -4.3; 206 -3.3; 227 -2.2; 249 -1.1; 274 -0.1; 302 0.7; 332 0.9; 365 0.8; 402 0.6; 442 0.8; 486 0.9; 535 0.4; 588 0.2; 647 0.1; 712 -0.1; 783 0.1; 861 0.3; 947 0.4; 1042 -0.1; 1146 0.4; 1261 0.3; 1387 -0.1; 1526 -0.4; 1678 -0.3; 1846 0.2; 2031 0.6; 2234 0.8; 2457 1.1; 2703 0.2; 2973 -2.2; 3270 -3.5; 3597 -3.6; 3957 -5.2; 4353 -4.4; 4788 -1.0; 5267 2.2; 5793 2.5; 6373 1.9; 7010 -0.1; 7711 -2.1; 8482 -6.5; 9330 -9.0; 10263 -5.5; 11289 -0.2; 12418 0.0; 13660 -0.8; 15026 -0.8; 16529 0.0; 18182 -1.7; 20000 -8.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G933 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-27**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G933 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 51 Hz    | 0.49 | -7.7 dB  |
| Peaking | 158 Hz   | 2.52 | -2.8 dB  |
| Peaking | 4103 Hz  | 2.45 | -8.8 dB  |
| Peaking | 5365 Hz  | 1.32 | 5.6 dB   |
| Peaking | 9137 Hz  | 3.26 | -10.6 dB |
| Peaking | 96 Hz    | 3.5  | -1.3 dB  |
| Peaking | 362 Hz   | 1.66 | 1.8 dB   |
| Peaking | 2479 Hz  | 3.32 | 1.7 dB   |
| Peaking | 3117 Hz  | 7.14 | -2.4 dB  |
| Peaking | 11483 Hz | 8.08 | 1.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Logitech%20G933/Logitech%20G933.png)