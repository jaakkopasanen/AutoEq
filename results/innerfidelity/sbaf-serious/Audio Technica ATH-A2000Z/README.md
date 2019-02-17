# Audio Technica ATH-A2000Z
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -1.3; 25 -2.0; 28 -2.9; 31 -3.6; 34 -4.2; 37 -4.8; 41 -5.4; 45 -5.8; 49 -6.2; 54 -6.5; 60 -6.9; 66 -7.0; 72 -7.2; 79 -7.3; 87 -7.6; 96 -8.4; 106 -9.0; 116 -9.1; 128 -9.1; 141 -9.1; 155 -8.8; 170 -8.1; 187 -8.3; 206 -7.9; 227 -7.3; 249 -6.9; 274 -6.5; 302 -6.3; 332 -6.3; 365 -6.3; 402 -6.6; 442 -6.5; 486 -6.7; 535 -6.7; 588 -6.4; 647 -6.4; 712 -6.6; 783 -6.3; 861 -6.2; 947 -6.5; 1042 -6.1; 1146 -6.3; 1261 -6.5; 1387 -7.2; 1526 -8.8; 1678 -10.4; 1846 -11.2; 2031 -11.6; 2234 -11.4; 2457 -9.2; 2703 -6.7; 2973 -5.0; 3270 -5.1; 3597 -8.1; 3957 -9.9; 4353 -9.7; 4788 -5.8; 5267 -0.5; 5793 -0.8; 6373 -1.5; 7010 -4.0; 7711 -6.2; 8482 -6.6; 9330 -11.4; 10263 -10.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -10.5; 18182 -8.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-A2000Z GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-A2000Z ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 2.2  | 6.0 dB   |
| Peaking | 2018 Hz  | 2.4  | -6.9 dB  |
| Peaking | 4242 Hz  | 3.16 | -12.5 dB |
| Peaking | 4927 Hz  | 1.11 | 9.9 dB   |
| Peaking | 9507 Hz  | 3.05 | -7.0 dB  |
| Peaking | 34 Hz    | 2.01 | 1.3 dB   |
| Peaking | 130 Hz   | 1.09 | -2.8 dB  |
| Peaking | 300 Hz   | 2.25 | 0.8 dB   |
| Peaking | 16886 Hz | 2.51 | -4.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -2.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-A2000Z/Audio%20Technica%20ATH-A2000Z.png)