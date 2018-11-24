# Logitech G933

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 21 -3.7; 23 -4.6; 25 -5.3; 28 -6.2; 31 -6.9; 34 -7.2; 37 -7.2; 41 -7.1; 45 -6.8; 49 -6.8; 54 -7.0; 60 -7.2; 66 -7.4; 72 -7.3; 79 -7.0; 87 -6.7; 96 -6.2; 106 -5.6; 116 -4.8; 128 -4.5; 141 -4.6; 155 -4.7; 170 -4.4; 187 -3.7; 206 -2.8; 227 -1.7; 249 -0.6; 274 0.5; 302 1.5; 332 1.9; 365 1.8; 402 1.6; 442 1.9; 486 2.1; 535 1.6; 588 1.3; 647 1.2; 712 0.8; 783 0.6; 861 0.5; 947 0.5; 1042 -0.0; 1146 0.6; 1261 0.5; 1387 -0.1; 1526 -0.7; 1678 -0.6; 1846 0.2; 2031 1.0; 2234 1.3; 2457 1.6; 2703 0.8; 2973 -1.2; 3270 -1.6; 3597 -1.4; 3957 -4.0; 4353 -4.4; 4788 -1.2; 5267 2.6; 5793 3.9; 6373 4.4; 7010 2.3; 7711 -1.0; 8482 -6.1; 9330 -7.5; 10263 -2.1; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.0; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G933 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-48**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G933 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 40 Hz   | 0.61 | -6.9 dB  |
| Peaking | 105 Hz  | 1.04 | -3.7 dB  |
| Peaking | 4297 Hz | 1.94 | -12.4 dB |
| Peaking | 5526 Hz | 0.89 | 10.6 dB  |
| Peaking | 8898 Hz | 2.93 | -12.2 dB |
| Peaking | 188 Hz  | 2.23 | -2.9 dB  |
| Peaking | 353 Hz  | 0.86 | 2.7 dB   |
| Peaking | 1612 Hz | 3.33 | -1.8 dB  |
| Peaking | 2479 Hz | 1.73 | 1.2 dB   |
| Peaking | 3079 Hz | 7.39 | -2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Logitech%20G933/Logitech%20G933.png)