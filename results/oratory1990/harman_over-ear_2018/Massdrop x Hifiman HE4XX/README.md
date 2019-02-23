# Massdrop x Hifiman HE4XX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.9; 41 -1.8; 45 -2.6; 49 -3.2; 54 -3.9; 60 -4.6; 66 -5.1; 72 -5.6; 79 -6.1; 87 -6.3; 96 -6.6; 106 -6.8; 116 -6.9; 128 -7.1; 141 -7.3; 155 -7.5; 170 -7.5; 187 -7.5; 206 -7.4; 227 -7.3; 249 -7.5; 274 -7.4; 302 -7.0; 332 -6.8; 365 -6.7; 402 -6.8; 442 -7.0; 486 -6.4; 535 -5.6; 588 -5.3; 647 -5.5; 712 -5.8; 783 -6.3; 861 -7.0; 947 -7.5; 1042 -7.8; 1146 -7.6; 1261 -7.1; 1387 -5.8; 1526 -4.0; 1678 -3.4; 1846 -2.7; 2031 -2.0; 2234 -4.2; 2457 -7.2; 2703 -9.4; 2973 -10.1; 3270 -9.4; 3597 -7.7; 3957 -6.7; 4353 -6.2; 4788 -3.6; 5267 -2.7; 5793 -5.6; 6373 -9.2; 7010 -9.4; 7711 -10.7; 8482 -7.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -9.5; 18182 -13.9; 20000 -15.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Hifiman HE4XX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Hifiman HE4XX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 1.13 | 6.9 dB  |
| Peaking | 1988 Hz | 2.79 | 5.9 dB  |
| Peaking | 2868 Hz | 2.23 | -4.8 dB |
| Peaking | 5166 Hz | 3.93 | 5.3 dB  |
| Peaking | 7085 Hz | 2.76 | -4.3 dB |
| Peaking | 184 Hz  | 0.87 | -1.2 dB |
| Peaking | 628 Hz  | 2.6  | 1.7 dB  |
| Peaking | 1113 Hz | 1.71 | -1.8 dB |
| Peaking | 1534 Hz | 5.13 | 2.0 dB  |
| Peaking | 3773 Hz | 3.57 | 0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Hifiman%20HE4XX/Massdrop%20x%20Hifiman%20HE4XX.png)