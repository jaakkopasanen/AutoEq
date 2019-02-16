# Hifiman Ananda
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 21 -1.9; 23 -2.1; 25 -2.3; 28 -2.6; 31 -2.8; 34 -2.9; 37 -3.0; 41 -3.1; 45 -3.0; 49 -2.9; 54 -3.0; 60 -4.1; 66 -4.5; 72 -4.6; 79 -4.7; 87 -5.0; 96 -5.3; 106 -5.6; 116 -5.9; 128 -6.2; 141 -6.5; 155 -6.7; 170 -7.0; 187 -7.2; 206 -7.4; 227 -7.5; 249 -6.9; 274 -6.9; 302 -6.9; 332 -6.4; 365 -5.6; 402 -6.6; 442 -6.5; 486 -7.2; 535 -7.8; 588 -7.9; 647 -7.4; 712 -4.2; 783 -4.2; 861 -5.7; 947 -6.7; 1042 -5.9; 1146 -2.9; 1261 -2.3; 1387 -1.0; 1526 -1.2; 1678 -0.5; 1846 -1.2; 2031 -1.7; 2234 -2.5; 2457 -4.1; 2703 -5.9; 2973 -6.8; 3270 -7.0; 3597 -6.4; 3957 -6.0; 4353 -6.2; 4788 -5.7; 5267 -3.9; 5793 -3.9; 6373 -6.9; 7010 -6.3; 7711 -6.1; 8482 -6.3; 9330 -6.4; 10263 -6.4; 11289 -8.7; 12418 -6.8; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -12.0; 20000 -18.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hifiman Ananda GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-64**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hifiman Ananda ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 1.03 | 4.0 dB   |
| Peaking | 50 Hz    | 1.52 | 2.5 dB   |
| Peaking | 1434 Hz  | 2.64 | 4.9 dB   |
| Peaking | 1955 Hz  | 3.11 | 4.1 dB   |
| Peaking | 5529 Hz  | 7.91 | 3.3 dB   |
| Peaking | 207 Hz   | 2.64 | -1.3 dB  |
| Peaking | 651 Hz   | 2.25 | -2.6 dB  |
| Peaking | 740 Hz   | 7.07 | 5.1 dB   |
| Peaking | 3108 Hz  | 5.88 | -1.5 dB  |
| Peaking | 19749 Hz | 1.4  | -12.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Hifiman%20Ananda/Hifiman%20Ananda.png)