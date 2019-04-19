# Hifiman HE35X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -4.4; 25 -5.0; 28 -5.7; 31 -6.4; 34 -6.9; 37 -7.3; 41 -7.8; 45 -8.2; 49 -8.5; 54 -8.8; 60 -9.0; 66 -9.1; 72 -9.0; 79 -8.7; 87 -9.0; 96 -10.2; 106 -11.2; 116 -11.8; 128 -12.2; 141 -12.5; 155 -12.6; 170 -12.6; 187 -12.5; 206 -12.7; 227 -12.8; 249 -12.4; 274 -11.8; 302 -11.2; 332 -10.5; 365 -9.7; 402 -9.0; 442 -8.1; 486 -7.2; 535 -6.4; 588 -5.7; 647 -4.8; 712 -3.5; 783 -3.2; 861 -3.1; 947 -2.8; 1042 -2.0; 1146 -1.1; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.6; 2234 -3.2; 2457 -6.3; 2703 -7.8; 2973 -8.4; 3270 -8.5; 3597 -9.5; 3957 -11.0; 4353 -11.8; 4788 -12.4; 5267 -13.5; 5793 -10.6; 6373 -3.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hifiman HE35X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hifiman HE35X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.47 | 3.9 dB  |
| Peaking | 58 Hz   | 0.25 | -1.3 dB |
| Peaking | 200 Hz  | 0.67 | -6.0 dB |
| Peaking | 1372 Hz | 0.76 | 7.0 dB  |
| Peaking | 4263 Hz | 1.7  | -7.3 dB |
| Peaking | 2073 Hz | 3.95 | 3.8 dB  |
| Peaking | 2580 Hz | 1.88 | -3.7 dB |
| Peaking | 4061 Hz | 1.6  | 2.4 dB  |
| Peaking | 5491 Hz | 3.72 | -5.9 dB |
| Peaking | 6567 Hz | 5.06 | 7.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -5.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -7.5 dB |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Hifiman%20HE35X/Hifiman%20HE35X.png)