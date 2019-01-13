# Ultrasone Edition 15
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.3; 25 2.5; 28 1.5; 31 0.7; 34 -0.1; 37 -0.7; 41 -1.3; 45 -1.8; 49 -2.3; 54 -3.0; 60 -3.7; 66 -4.0; 72 -4.4; 79 -4.8; 87 -5.5; 96 -5.9; 106 -6.4; 116 -6.5; 128 -6.6; 141 -6.4; 155 -6.2; 170 -5.7; 187 -5.5; 206 -5.2; 227 -4.9; 249 -4.7; 274 -4.0; 302 -3.8; 332 -3.2; 365 -2.7; 402 -1.9; 442 -2.7; 486 -3.2; 535 -2.7; 588 -2.2; 647 -1.6; 712 -1.0; 783 -0.6; 861 -0.4; 947 -0.2; 1042 0.3; 1146 0.8; 1261 1.3; 1387 1.8; 1526 2.0; 1678 1.9; 1846 2.3; 2031 1.0; 2234 -0.5; 2457 -0.0; 2703 5.4; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.8; 4353 3.0; 4788 2.1; 5267 0.5; 5793 2.7; 6373 5.4; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.2; 13660 -6.3; 15026 -6.4; 16529 -2.8; 18182 -1.6; 20000 -0.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone Edition 15 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Edition 15 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.82 | 6.2 dB  |
| Peaking | 128 Hz   | 0.44 | -6.5 dB |
| Peaking | 3365 Hz  | 1.94 | 6.7 dB  |
| Peaking | 6415 Hz  | 6.93 | 5.2 dB  |
| Peaking | 14645 Hz | 2.88 | -7.9 dB |
| Peaking | 531 Hz   | 3.54 | -1.5 dB |
| Peaking | 1830 Hz  | 1.06 | 2.1 dB  |
| Peaking | 2304 Hz  | 5.17 | -4.7 dB |
| Peaking | 5212 Hz  | 8.2  | -1.7 dB |
| Peaking | 11973 Hz | 7.79 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Ultrasone%20Edition%2015/Ultrasone%20Edition%2015.png)