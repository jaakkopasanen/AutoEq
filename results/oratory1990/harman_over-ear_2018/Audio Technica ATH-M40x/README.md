# Audio Technica ATH-M40x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.9; 45 5.2; 49 4.0; 54 2.8; 60 2.3; 66 2.5; 72 2.0; 79 0.5; 87 -0.4; 96 -0.4; 106 -1.9; 116 -2.9; 128 -3.7; 141 -3.9; 155 -3.9; 170 -4.2; 187 -4.4; 206 -4.2; 227 -4.0; 249 -3.5; 274 -2.7; 302 -1.7; 332 -0.6; 365 0.2; 402 -0.4; 442 -0.4; 486 -0.3; 535 -0.3; 588 -0.2; 647 -0.2; 712 -0.2; 783 -0.2; 861 -0.3; 947 -0.2; 1042 -0.2; 1146 -0.9; 1261 -1.3; 1387 -1.6; 1526 -1.3; 1678 -1.3; 1846 -0.9; 2031 -0.5; 2234 -0.4; 2457 -0.8; 2703 -1.1; 2973 -1.1; 3270 -0.9; 3597 -0.7; 3957 -1.0; 4353 -2.7; 4788 -1.4; 5267 -1.3; 5793 -1.4; 6373 -2.4; 7010 -3.7; 7711 -5.2; 8482 -4.9; 9330 -2.9; 10263 -0.9; 11289 -0.7; 12418 -4.2; 13660 -8.1; 15026 -8.0; 16529 -5.9; 18182 -6.2; 20000 -12.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M40x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M40x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.61 | 6.6 dB  |
| Peaking | 160 Hz   | 0.99 | -5.3 dB |
| Peaking | 1470 Hz  | 2.27 | -1.4 dB |
| Peaking | 14277 Hz | 5.27 | -3.4 dB |
| Peaking | 22197 Hz | 0.1  | -7.5 dB |
| Peaking | 248 Hz   | 3.83 | -1.2 dB |
| Peaking | 359 Hz   | 3.56 | 1.3 dB  |
| Peaking | 7926 Hz  | 2.98 | -3.4 dB |
| Peaking | 10793 Hz | 3.96 | 4.3 dB  |
| Peaking | 20059 Hz | 4.49 | -5.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audio%20Technica%20ATH-M40x/Audio%20Technica%20ATH-M40x.png)