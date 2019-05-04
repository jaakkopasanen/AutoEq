# Audio-Technica ATH-MSR7NC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.1; 28 -1.5; 31 -1.7; 34 -1.9; 37 -2.0; 41 -2.0; 45 -2.0; 49 -2.1; 54 -2.2; 60 -2.5; 66 -2.9; 72 -3.2; 79 -3.7; 87 -4.2; 96 -4.7; 106 -5.1; 116 -5.5; 128 -5.8; 141 -5.9; 155 -6.1; 170 -6.1; 187 -6.0; 206 -5.8; 227 -5.6; 249 -5.3; 274 -4.8; 302 -3.5; 332 -2.1; 365 -1.1; 402 -1.1; 442 -1.7; 486 -2.3; 535 -2.7; 588 -3.1; 647 -3.3; 712 -3.5; 783 -3.6; 861 -3.8; 947 -4.2; 1042 -4.6; 1146 -4.9; 1261 -5.5; 1387 -6.2; 1526 -7.4; 1678 -8.5; 1846 -9.4; 2031 -10.1; 2234 -9.8; 2457 -8.4; 2703 -7.1; 2973 -6.2; 3270 -5.2; 3597 -3.8; 3957 -3.8; 4353 -6.8; 4788 -7.9; 5267 -6.3; 5793 -3.7; 6373 -1.9; 7010 -5.0; 7711 -8.7; 8482 -7.7; 9330 -5.3; 10263 -5.3; 11289 -5.3; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -5.2; 18182 -5.2; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-MSR7NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-MSR7NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.13 | 4.5 dB  |
| Peaking | 53 Hz    | 1.98 | 2.5 dB  |
| Peaking | 438 Hz   | 1.59 | 4.1 dB  |
| Peaking | 2027 Hz  | 2.55 | -5.4 dB |
| Peaking | 21228 Hz | 2.06 | -1.2 dB |
| Peaking | 172 Hz   | 1.83 | -1.6 dB |
| Peaking | 3823 Hz  | 4.61 | 3.6 dB  |
| Peaking | 4712 Hz  | 2.91 | -3.8 dB |
| Peaking | 6340 Hz  | 3.47 | 5.0 dB  |
| Peaking | 7769 Hz  | 4.43 | -4.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.0 dB |
| Peaking | 500 Hz   | 1.41 | 3.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-MSR7NC/Audio-Technica%20ATH-MSR7NC.png)