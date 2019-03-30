# Audio-Technica ATH-AD2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.9; 60 -1.4; 66 -1.9; 72 -2.2; 79 -2.6; 87 -2.9; 96 -3.2; 106 -3.5; 116 -3.9; 128 -4.1; 141 -4.4; 155 -4.7; 170 -4.8; 187 -5.1; 206 -5.2; 227 -5.4; 249 -5.5; 274 -5.8; 302 -5.9; 332 -6.1; 365 -6.1; 402 -6.1; 442 -6.1; 486 -6.1; 535 -6.1; 588 -6.1; 647 -6.1; 712 -6.1; 783 -6.3; 861 -6.5; 947 -6.5; 1042 -6.5; 1146 -6.4; 1261 -6.4; 1387 -6.4; 1526 -6.4; 1678 -6.4; 1846 -6.5; 2031 -6.4; 2234 -6.1; 2457 -5.8; 2703 -5.8; 2973 -6.3; 3270 -8.8; 3597 -12.2; 3957 -13.3; 4353 -11.8; 4788 -9.0; 5267 -6.5; 5793 -4.9; 6373 -4.9; 7010 -6.2; 7711 -7.7; 8482 -8.6; 9330 -9.2; 10263 -10.2; 11289 -11.4; 12418 -11.6; 13660 -10.0; 15026 -7.7; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-AD2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-AD2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.32 | 6.2 dB  |
| Peaking | 2918 Hz  | 2.13 | 3.5 dB  |
| Peaking | 3870 Hz  | 2.23 | -8.6 dB |
| Peaking | 5916 Hz  | 2.8  | 3.9 dB  |
| Peaking | 11723 Hz | 1.43 | -5.3 dB |
| Peaking | 637 Hz   | 2.53 | 0.3 dB  |
| Peaking | 8335 Hz  | 7.28 | -0.6 dB |
| Peaking | 16336 Hz | 2.94 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.8 dB  |
| Peaking | 125 Hz   | 1.41 | 1.6 dB  |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.1 dB |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-AD2000/Audio-Technica%20ATH-AD2000.png)