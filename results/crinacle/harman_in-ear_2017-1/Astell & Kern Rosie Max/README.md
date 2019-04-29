# Astell & Kern Rosie Max
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.8; 23 -13.9; 25 -14.0; 28 -14.2; 31 -14.3; 34 -14.3; 37 -14.4; 41 -14.5; 45 -14.6; 49 -14.6; 54 -14.7; 60 -14.8; 66 -15.0; 72 -15.2; 79 -15.3; 87 -15.6; 96 -15.7; 106 -15.8; 116 -15.8; 128 -15.8; 141 -15.8; 155 -15.7; 170 -15.5; 187 -15.3; 206 -14.9; 227 -14.5; 249 -14.1; 274 -13.6; 302 -13.1; 332 -12.4; 365 -11.7; 402 -11.0; 442 -10.4; 486 -9.7; 535 -8.9; 588 -8.2; 647 -7.4; 712 -6.5; 783 -5.6; 861 -4.9; 947 -4.4; 1042 -4.2; 1146 -4.5; 1261 -5.4; 1387 -5.7; 1526 -5.1; 1678 -4.4; 1846 -3.8; 2031 -3.1; 2234 -2.0; 2457 -1.1; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.2; 9330 -7.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.3; 15026 -13.7; 16529 -14.0; 18182 -19.6; 20000 -27.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astell & Kern Rosie Max GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astell & Kern Rosie Max ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.31 | -6.0 dB  |
| Peaking | 170 Hz   | 0.42 | -7.9 dB  |
| Peaking | 890 Hz   | 1.72 | 3.0 dB   |
| Peaking | 3599 Hz  | 0.88 | 7.0 dB   |
| Peaking | 18 Hz    | 0.86 | -0.8 dB  |
| Peaking | 2404 Hz  | 6.08 | 1.1 dB   |
| Peaking | 5977 Hz  | 4.94 | 3.4 dB   |
| Peaking | 19694 Hz | 0.5  | -8.6 dB  |
| Peaking | 19965 Hz | 0.62 | -11.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -7.6 dB  |
| Peaking | 62 Hz    | 1.41 | -6.0 dB  |
| Peaking | 125 Hz   | 1.41 | -7.7 dB  |
| Peaking | 250 Hz   | 1.41 | -6.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 16000 Hz | 1.41 | -10.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Astell%20&%20Kern%20Rosie%20Max/Astell%20&%20Kern%20Rosie%20Max.png)