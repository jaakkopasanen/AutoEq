# Audio Technica ATH-MSR7NC ANC Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.9; 23 -1.4; 25 -1.9; 28 -2.5; 31 -3.0; 34 -3.4; 37 -3.7; 41 -4.0; 45 -4.3; 49 -4.5; 54 -4.7; 60 -4.9; 66 -5.1; 72 -5.3; 79 -5.5; 87 -5.7; 96 -5.8; 106 -6.0; 116 -6.4; 128 -6.9; 141 -7.3; 155 -7.5; 170 -6.6; 187 -7.4; 206 -7.5; 227 -7.4; 249 -7.2; 274 -6.7; 302 -6.0; 332 -5.0; 365 -3.9; 402 -3.2; 442 -2.6; 486 -2.8; 535 -2.9; 588 -3.0; 647 -3.7; 712 -4.6; 783 -5.2; 861 -6.1; 947 -6.9; 1042 -7.6; 1146 -8.0; 1261 -8.5; 1387 -9.8; 1526 -10.7; 1678 -11.3; 1846 -11.6; 2031 -11.2; 2234 -10.2; 2457 -8.2; 2703 -6.4; 2973 -4.8; 3270 -4.1; 3597 -3.8; 3957 -4.8; 4353 -8.7; 4788 -9.0; 5267 -5.3; 5793 -0.5; 6373 -0.8; 7010 -3.7; 7711 -6.0; 8482 -8.1; 9330 -9.7; 10263 -7.4; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-MSR7NC ANC Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-MSR7NC ANC Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.88 | 5.2 dB  |
| Peaking | 509 Hz  | 1.91 | 4.2 dB  |
| Peaking | 1726 Hz | 2    | -6.0 dB |
| Peaking | 6194 Hz | 4.74 | 6.9 dB  |
| Peaking | 9275 Hz | 4.69 | -4.0 dB |
| Peaking | 216 Hz  | 1.23 | -1.7 dB |
| Peaking | 374 Hz  | 3.68 | 1.6 dB  |
| Peaking | 2220 Hz | 4.09 | -2.3 dB |
| Peaking | 3702 Hz | 1.55 | 4.2 dB  |
| Peaking | 4552 Hz | 4.44 | -6.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 4.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-MSR7NC%20ANC%20Active/Audio%20Technica%20ATH-MSR7NC%20ANC%20Active.png)