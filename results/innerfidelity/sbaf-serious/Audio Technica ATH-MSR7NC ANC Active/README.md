# Audio Technica ATH-MSR7NC ANC Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.0; 28 -1.6; 31 -2.1; 34 -2.5; 37 -2.8; 41 -3.1; 45 -3.4; 49 -3.5; 54 -3.7; 60 -4.0; 66 -4.2; 72 -4.4; 79 -4.6; 87 -4.8; 96 -4.9; 106 -5.1; 116 -5.4; 128 -6.0; 141 -6.4; 155 -6.6; 170 -5.7; 187 -6.4; 206 -6.6; 227 -6.5; 249 -6.3; 274 -5.8; 302 -5.1; 332 -4.0; 365 -3.0; 402 -2.3; 442 -1.7; 486 -1.8; 535 -2.0; 588 -2.1; 647 -2.7; 712 -3.6; 783 -4.3; 861 -5.2; 947 -6.0; 1042 -6.7; 1146 -7.1; 1261 -7.5; 1387 -8.8; 1526 -9.8; 1678 -10.4; 1846 -10.6; 2031 -10.3; 2234 -9.2; 2457 -7.2; 2703 -5.5; 2973 -3.9; 3270 -3.2; 3597 -2.8; 3957 -3.9; 4353 -7.7; 4788 -8.0; 5267 -4.4; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.1; 8482 -7.2; 9330 -8.8; 10263 -6.9; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-MSR7NC ANC Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-MSR7NC ANC Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.37 | 6.2 dB  |
| Peaking | 517 Hz  | 1.35 | 5.2 dB  |
| Peaking | 1815 Hz | 1.53 | -4.9 dB |
| Peaking | 3238 Hz | 3.14 | 4.8 dB  |
| Peaking | 6108 Hz | 5.3  | 6.8 dB  |
| Peaking | 230 Hz  | 1.79 | -1.1 dB |
| Peaking | 371 Hz  | 4.28 | 1.1 dB  |
| Peaking | 4638 Hz | 5.23 | -6.1 dB |
| Peaking | 4720 Hz | 1.84 | 2.7 dB  |
| Peaking | 9246 Hz | 4.91 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 5.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-MSR7NC%20ANC%20Active/Audio%20Technica%20ATH-MSR7NC%20ANC%20Active.png)