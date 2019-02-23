# Audio Technica ATH-MSR7NC Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.2; 23 -1.7; 25 -2.2; 28 -2.8; 31 -3.2; 34 -3.6; 37 -3.9; 41 -4.3; 45 -4.5; 49 -4.7; 54 -4.9; 60 -5.2; 66 -5.4; 72 -5.5; 79 -5.7; 87 -5.8; 96 -6.0; 106 -6.3; 116 -6.2; 128 -6.7; 141 -7.3; 155 -7.5; 170 -6.7; 187 -7.3; 206 -7.4; 227 -7.2; 249 -6.9; 274 -6.3; 302 -5.4; 332 -4.3; 365 -3.2; 402 -2.2; 442 -1.7; 486 -2.0; 535 -2.4; 588 -2.9; 647 -3.7; 712 -4.6; 783 -5.3; 861 -6.2; 947 -6.9; 1042 -7.5; 1146 -7.8; 1261 -8.1; 1387 -9.2; 1526 -10.3; 1678 -11.0; 1846 -11.1; 2031 -10.9; 2234 -9.7; 2457 -7.8; 2703 -5.9; 2973 -4.4; 3270 -3.6; 3597 -3.0; 3957 -3.7; 4353 -7.5; 4788 -7.9; 5267 -5.2; 5793 -0.9; 6373 -0.5; 7010 -3.4; 7711 -5.9; 8482 -7.8; 9330 -8.7; 10263 -6.3; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-MSR7NC Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-MSR7NC Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 1.19 | 4.6 dB  |
| Peaking | 514 Hz   | 1.57 | 5.3 dB  |
| Peaking | 3023 Hz  | 0.51 | -9.0 dB |
| Peaking | 3301 Hz  | 1.73 | 11.8 dB |
| Peaking | 6181 Hz  | 3.48 | 9.7 dB  |
| Peaking | 204 Hz   | 1.2  | -1.9 dB |
| Peaking | 378 Hz   | 3.5  | 1.7 dB  |
| Peaking | 1789 Hz  | 5.66 | -1.2 dB |
| Peaking | 9237 Hz  | 4.17 | -3.2 dB |
| Peaking | 10294 Hz | 1.42 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 5.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-MSR7NC%20Passive/Audio%20Technica%20ATH-MSR7NC%20Passive.png)