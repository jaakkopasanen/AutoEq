# Massdrop x Hifiman HE4XX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.4; 49 -2.0; 54 -2.7; 60 -3.4; 66 -3.9; 72 -4.4; 79 -4.9; 87 -5.2; 96 -5.4; 106 -5.6; 116 -5.7; 128 -5.9; 141 -6.1; 155 -6.3; 170 -6.3; 187 -6.3; 206 -6.3; 227 -6.1; 249 -6.3; 274 -6.2; 302 -5.9; 332 -5.6; 365 -5.5; 402 -5.6; 442 -5.8; 486 -5.2; 535 -4.4; 588 -4.1; 647 -4.3; 712 -4.6; 783 -5.2; 861 -5.8; 947 -6.4; 1042 -6.6; 1146 -6.5; 1261 -5.9; 1387 -4.7; 1526 -2.9; 1678 -2.2; 1846 -1.6; 2031 -0.8; 2234 -3.1; 2457 -6.1; 2703 -8.3; 2973 -8.9; 3270 -8.3; 3597 -6.5; 3957 -5.6; 4353 -5.1; 4788 -2.4; 5267 -1.6; 5793 -4.4; 6373 -8.0; 7010 -8.2; 7711 -9.5; 8482 -6.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -8.3; 18182 -12.8; 20000 -14.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Hifiman HE4XX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Hifiman HE4XX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.72 | 6.6 dB  |
| Peaking | 618 Hz   | 1.57 | 3.0 dB  |
| Peaking | 1899 Hz  | 1.71 | 10.1 dB |
| Peaking | 2947 Hz  | 0.43 | -5.6 dB |
| Peaking | 4942 Hz  | 2.51 | 8.8 dB  |
| Peaking | 2863 Hz  | 5.39 | -1.3 dB |
| Peaking | 3746 Hz  | 6.85 | 1.8 dB  |
| Peaking | 7762 Hz  | 3.42 | -3.0 dB |
| Peaking | 8619 Hz  | 3.57 | 2.5 dB  |
| Peaking | 11104 Hz | 2.85 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -2.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Hifiman%20HE4XX/Massdrop%20x%20Hifiman%20HE4XX.png)