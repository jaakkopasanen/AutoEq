# Logitech G533

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.4dB
GraphicEQ: 21 -3.5; 23 -3.7; 25 -3.9; 28 -4.2; 31 -4.4; 34 -4.4; 37 -4.4; 41 -4.2; 45 -4.1; 49 -4.0; 54 -3.9; 60 -3.9; 66 -4.0; 72 -4.0; 79 -4.1; 87 -4.3; 96 -4.5; 106 -4.7; 116 -4.8; 128 -4.8; 141 -4.7; 155 -4.7; 170 -4.6; 187 -4.5; 206 -4.2; 227 -4.0; 249 -4.0; 274 -4.3; 302 -4.7; 332 -4.7; 365 -4.2; 402 -3.4; 442 -2.8; 486 -2.4; 535 -1.7; 588 -1.1; 647 -0.8; 712 -0.3; 783 0.7; 861 1.1; 947 0.3; 1042 -0.2; 1146 -0.5; 1261 -0.1; 1387 1.1; 1526 2.2; 1678 1.6; 1846 0.6; 2031 -0.2; 2234 -0.0; 2457 0.5; 2703 -2.3; 2973 -1.7; 3270 -1.0; 3597 -1.8; 3957 -2.6; 4353 -3.2; 4788 -0.7; 5267 1.9; 5793 1.3; 6373 -1.9; 7010 -2.1; 7711 -2.0; 8482 -6.0; 9330 -7.6; 10263 -2.8; 11289 0.0; 12418 -1.8; 13660 -4.2; 15026 -2.9; 16529 -2.4; 18182 -5.6; 20000 -9.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G533 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-24**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G533 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.42 | -3.9 dB  |
| Peaking | 144 Hz   | 0.8  | -3.7 dB  |
| Peaking | 335 Hz   | 1.78 | -3.5 dB  |
| Peaking | 9023 Hz  | 4.54 | -7.9 dB  |
| Peaking | 20685 Hz | 0.72 | -10.4 dB |
| Peaking | 1563 Hz  | 6.57 | 2.3 dB   |
| Peaking | 2765 Hz  | 8.4  | -2.1 dB  |
| Peaking | 2849 Hz  | 0.37 | 0.7 dB   |
| Peaking | 4556 Hz  | 1.58 | -4.2 dB  |
| Peaking | 5300 Hz  | 4.87 | 5.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Logitech%20G533/Logitech%20G533.png)