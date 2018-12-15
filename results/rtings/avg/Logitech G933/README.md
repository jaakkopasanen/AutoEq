# Logitech G933

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.3dB
GraphicEQ: 21 -4.1; 23 -4.9; 25 -5.6; 28 -6.4; 31 -6.9; 34 -7.2; 37 -7.1; 41 -6.8; 45 -6.6; 49 -6.5; 54 -6.7; 60 -6.9; 66 -7.2; 72 -7.3; 79 -7.2; 87 -7.0; 96 -6.7; 106 -6.0; 116 -5.4; 128 -5.0; 141 -5.2; 155 -5.3; 170 -5.1; 187 -4.3; 206 -3.3; 227 -2.2; 249 -1.1; 274 -0.1; 302 0.7; 332 0.9; 365 0.8; 402 0.6; 442 0.8; 486 0.9; 535 0.4; 588 0.2; 647 0.1; 712 -0.1; 783 0.1; 861 0.3; 947 0.4; 1042 -0.1; 1146 0.4; 1261 0.3; 1387 -0.1; 1526 -0.4; 1678 -0.3; 1846 0.2; 2031 0.6; 2234 0.8; 2457 1.1; 2703 -0.1; 2973 -2.7; 3270 -4.2; 3597 -4.6; 3957 -6.5; 4353 -5.7; 4788 -2.8; 5267 -0.4; 5793 0.1; 6373 0.7; 7010 -1.0; 7711 -3.5; 8482 -7.1; 9330 -7.7; 10263 -3.8; 11289 -0.3; 12418 -1.3; 13660 -4.0; 15026 -3.4; 16529 -2.2; 18182 -6.0; 20000 -14.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G933 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-12**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G933 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 51 Hz    | 0.49 | -7.7 dB  |
| Peaking | 158 Hz   | 2.51 | -2.8 dB  |
| Peaking | 3948 Hz  | 3.53 | -6.8 dB  |
| Peaking | 8909 Hz  | 4.24 | -8.3 dB  |
| Peaking | 20162 Hz | 1.32 | -14.4 dB |
| Peaking | 363 Hz   | 1.82 | 1.8 dB   |
| Peaking | 2900 Hz  | 1.55 | 3.2 dB   |
| Peaking | 3095 Hz  | 5.67 | -4.5 dB  |
| Peaking | 5281 Hz  | 0.85 | -2.2 dB  |
| Peaking | 6034 Hz  | 2.6  | 3.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Logitech%20G933/Logitech%20G933.png)