# Audio Technica ATH-M50x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.9; 25 5.3; 28 4.0; 31 2.9; 34 2.0; 37 1.3; 41 0.7; 45 0.4; 49 0.4; 54 0.6; 60 0.7; 66 0.2; 72 -0.0; 79 0.3; 87 -0.3; 96 -1.4; 106 -2.2; 116 -2.3; 128 -2.5; 141 -3.0; 155 -3.2; 170 -3.1; 187 -2.7; 206 -1.9; 227 -0.6; 249 1.0; 274 2.4; 302 2.9; 332 2.4; 365 2.0; 402 1.3; 442 0.7; 486 0.3; 535 0.1; 588 -0.0; 647 -0.0; 712 0.0; 783 0.1; 861 0.1; 947 0.1; 1042 -0.1; 1146 -0.4; 1261 -0.7; 1387 -0.7; 1526 -0.6; 1678 -0.7; 1846 -1.1; 2031 -1.7; 2234 -2.5; 2457 -3.4; 2703 -3.6; 2973 -3.6; 3270 -2.4; 3597 -0.6; 3957 -2.1; 4353 -5.0; 4788 -2.4; 5267 0.2; 5793 1.2; 6373 -1.3; 7010 -4.2; 7711 -5.0; 8482 -3.0; 9330 -0.1; 10263 0.0; 11289 -2.4; 12418 -7.5; 13660 -11.0; 15026 -12.0; 16529 -9.9; 18182 -8.3; 20000 -12.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M50x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M50x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 2.15 | 6.8 dB   |
| Peaking | 2632 Hz  | 2.39 | -3.8 dB  |
| Peaking | 4355 Hz  | 7.45 | -4.3 dB  |
| Peaking | 14577 Hz | 1.9  | -10.1 dB |
| Peaking | 20545 Hz | 0.71 | -12.0 dB |
| Peaking | 165 Hz   | 1.25 | -4.0 dB  |
| Peaking | 298 Hz   | 1.99 | 4.1 dB   |
| Peaking | 5800 Hz  | 4.84 | 3.6 dB   |
| Peaking | 7509 Hz  | 2.58 | -4.8 dB  |
| Peaking | 9978 Hz  | 3.57 | 4.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audio%20Technica%20ATH-M50x/Audio%20Technica%20ATH-M50x.png)