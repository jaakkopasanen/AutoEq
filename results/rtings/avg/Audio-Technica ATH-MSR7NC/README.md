# Audio-Technica ATH-MSR7NC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.1; 28 -1.5; 31 -1.7; 34 -1.8; 37 -1.8; 41 -1.9; 45 -1.9; 49 -2.0; 54 -2.2; 60 -2.4; 66 -2.8; 72 -3.2; 79 -3.7; 87 -4.2; 96 -4.6; 106 -5.1; 116 -5.4; 128 -5.7; 141 -5.8; 155 -6.0; 170 -6.0; 187 -5.9; 206 -5.7; 227 -5.4; 249 -5.1; 274 -4.6; 302 -3.3; 332 -2.0; 365 -0.9; 402 -0.9; 442 -1.5; 486 -2.0; 535 -2.4; 588 -2.7; 647 -2.9; 712 -3.1; 783 -3.3; 861 -3.5; 947 -3.9; 1042 -4.2; 1146 -4.5; 1261 -5.1; 1387 -5.7; 1526 -6.9; 1678 -8.0; 1846 -8.9; 2031 -9.4; 2234 -8.8; 2457 -7.2; 2703 -6.3; 2973 -5.8; 3270 -5.2; 3597 -3.8; 3957 -3.8; 4353 -7.0; 4788 -7.2; 5267 -5.7; 5793 -3.6; 6373 -2.6; 7010 -4.6; 7711 -7.6; 8482 -7.9; 9330 -6.7; 10263 -5.5; 11289 -4.2; 12418 -4.1; 13660 -4.1; 15026 -4.1; 16529 -4.1; 18182 -4.1; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-MSR7NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-MSR7NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.02 | 3.3 dB  |
| Peaking | 420 Hz   | 2.53 | 3.5 dB  |
| Peaking | 1990 Hz  | 2.17 | -5.6 dB |
| Peaking | 4680 Hz  | 6.49 | -3.4 dB |
| Peaking | 21080 Hz | 2.04 | -2.1 dB |
| Peaking | 56 Hz    | 2.06 | 1.4 dB  |
| Peaking | 156 Hz   | 1.34 | -2.4 dB |
| Peaking | 6487 Hz  | 3.87 | 3.7 dB  |
| Peaking | 8139 Hz  | 2.23 | -4.7 dB |
| Peaking | 11872 Hz | 2.62 | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-MSR7NC/Audio-Technica%20ATH-MSR7NC.png)