# 1MORE Triple Driver In-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 0.0; 23 0.5; 25 0.3; 28 -0.1; 31 -0.3; 34 -0.5; 37 -0.7; 41 -0.9; 45 -1.0; 49 -1.1; 54 -1.3; 60 -1.8; 66 -2.1; 72 -2.5; 79 -2.8; 87 -3.3; 96 -3.8; 106 -4.3; 116 -4.8; 128 -5.2; 141 -5.5; 155 -5.6; 170 -5.5; 187 -5.4; 206 -5.2; 227 -5.2; 249 -5.0; 274 -4.5; 302 -4.0; 332 -3.4; 365 -2.8; 402 -2.1; 442 -1.4; 486 -0.7; 535 0.1; 588 0.8; 647 1.3; 712 1.4; 783 1.3; 861 0.9; 947 0.3; 1042 -0.2; 1146 -0.4; 1261 -0.7; 1387 -1.0; 1526 -1.4; 1678 -2.0; 1846 -2.8; 2031 -3.6; 2234 -3.6; 2457 -3.0; 2703 -2.0; 2973 -1.1; 3270 -1.1; 3597 -2.0; 3957 -4.0; 4353 -6.2; 4788 -3.2; 5267 3.4; 5793 5.9; 6373 4.9; 7010 2.5; 7711 0.3; 8482 -1.6; 9330 -3.0; 10263 -2.9; 11289 -1.7; 12418 -0.9; 13660 -2.6; 15026 -6.1; 16529 -7.8; 18182 -8.5; 20000 -11.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Triple Driver In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Triple Driver In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 163 Hz   | 0.74 | -6.0 dB  |
| Peaking | 2127 Hz  | 2.58 | -3.8 dB  |
| Peaking | 4436 Hz  | 3.92 | -8.3 dB  |
| Peaking | 5804 Hz  | 2.9  | 8.6 dB   |
| Peaking | 20014 Hz | 0.49 | -10.8 dB |
| Peaking | 18 Hz    | 1.9  | 1.0 dB   |
| Peaking | 307 Hz   | 2.36 | -1.2 dB  |
| Peaking | 678 Hz   | 2.15 | 2.4 dB   |
| Peaking | 9453 Hz  | 4.36 | -2.2 dB  |
| Peaking | 12557 Hz | 4.41 | 2.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/1MORE%20Triple%20Driver%20In-Ear/1MORE%20Triple%20Driver%20In-Ear.png)