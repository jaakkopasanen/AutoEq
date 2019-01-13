# 64 Audio N8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 0.0; 23 -0.6; 25 -1.1; 28 -1.2; 31 -1.2; 34 -1.4; 37 -1.4; 41 -1.5; 45 -1.7; 49 -1.8; 54 -2.2; 60 -2.4; 66 -2.8; 72 -2.7; 79 -3.0; 87 -3.2; 96 -2.7; 106 -3.1; 116 -3.0; 128 -3.1; 141 -3.1; 155 -3.1; 170 -3.1; 187 -3.3; 206 -3.3; 227 -3.2; 249 -3.2; 274 -3.2; 302 -3.0; 332 -2.9; 365 -2.6; 402 -2.5; 442 -2.4; 486 -2.1; 535 -1.9; 588 -1.6; 647 -1.2; 712 -0.8; 783 -0.4; 861 0.0; 947 0.1; 1042 -0.2; 1146 -0.8; 1261 -1.6; 1387 -2.0; 1526 -2.1; 1678 -1.9; 1846 -1.6; 2031 -1.0; 2234 0.1; 2457 1.5; 2703 2.9; 2973 4.0; 3270 4.6; 3597 4.5; 3957 3.7; 4353 2.8; 4788 1.9; 5267 2.4; 5793 5.8; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.0; 13660 -9.9; 15026 -19.8; 16529 -19.0; 18182 -11.9; 20000 -3.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 142 Hz   | 0.44 | -1.8 dB  |
| Peaking | 369 Hz   | 0.09 | -1.6 dB  |
| Peaking | 5665 Hz  | 0.6  | 7.1 dB   |
| Peaking | 12140 Hz | 2.41 | 10.6 dB  |
| Peaking | 15478 Hz | 1.09 | -25.0 dB |
| Peaking | 951 Hz   | 1.16 | 4.7 dB   |
| Peaking | 1485 Hz  | 0.55 | -4.5 dB  |
| Peaking | 3200 Hz  | 1.33 | 5.2 dB   |
| Peaking | 5297 Hz  | 1.7  | -5.4 dB  |
| Peaking | 5911 Hz  | 3.94 | 6.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/64%20Audio%20N8/64%20Audio%20N8.png)