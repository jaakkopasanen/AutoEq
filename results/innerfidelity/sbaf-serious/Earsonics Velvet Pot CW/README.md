# Earsonics Velvet Pot CW
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.4; 23 -12.7; 25 -12.9; 28 -13.2; 31 -13.3; 34 -13.4; 37 -13.5; 41 -13.6; 45 -13.7; 49 -13.8; 54 -13.9; 60 -14.0; 66 -14.0; 72 -14.0; 79 -14.1; 87 -14.0; 96 -13.9; 106 -13.5; 116 -13.1; 128 -12.6; 141 -11.9; 155 -11.1; 170 -10.2; 187 -9.1; 206 -8.0; 227 -6.8; 249 -5.9; 274 -5.2; 302 -4.9; 332 -5.1; 365 -5.4; 402 -5.9; 442 -6.4; 486 -7.0; 535 -7.3; 588 -7.2; 647 -7.5; 712 -7.8; 783 -7.8; 861 -8.3; 947 -8.7; 1042 -9.2; 1146 -9.6; 1261 -10.0; 1387 -10.5; 1526 -10.8; 1678 -10.6; 1846 -9.6; 2031 -7.6; 2234 -5.7; 2457 -4.4; 2703 -2.7; 2973 -1.3; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -1.0; 4788 -3.4; 5267 -1.0; 5793 -0.5; 6373 -2.3; 7010 -6.9; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics Velvet Pot CW GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics Velvet Pot CW ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.57 | -7.1 dB |
| Peaking | 103 Hz  | 1.33 | -5.2 dB |
| Peaking | 1529 Hz | 1.32 | -5.5 dB |
| Peaking | 3371 Hz | 1.38 | 7.2 dB  |
| Peaking | 5745 Hz | 5.34 | 4.9 dB  |
| Peaking | 36 Hz   | 2.65 | 0.7 dB  |
| Peaking | 64 Hz   | 3.72 | -0.9 dB |
| Peaking | 160 Hz  | 3.35 | -1.5 dB |
| Peaking | 292 Hz  | 2.12 | 2.7 dB  |
| Peaking | 7203 Hz | 6.47 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.5 dB |
| Peaking | 62 Hz    | 1.41 | -6.0 dB |
| Peaking | 125 Hz   | 1.41 | -6.1 dB |
| Peaking | 250 Hz   | 1.41 | 2.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.2 dB |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Earsonics%20Velvet%20Pot%20CW/Earsonics%20Velvet%20Pot%20CW.png)