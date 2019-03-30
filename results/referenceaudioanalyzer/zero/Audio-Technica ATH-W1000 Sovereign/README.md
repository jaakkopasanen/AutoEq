# Audio-Technica ATH-W1000 Sovereign
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.7; 72 -1.1; 79 -1.5; 87 -1.8; 96 -2.0; 106 -2.1; 116 -1.9; 128 -1.7; 141 -1.6; 155 -1.3; 170 -0.8; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -1.4; 302 -2.7; 332 -3.3; 365 -4.1; 402 -5.5; 442 -6.8; 486 -7.7; 535 -8.1; 588 -8.2; 647 -8.0; 712 -7.9; 783 -8.0; 861 -8.4; 947 -8.6; 1042 -8.8; 1146 -8.9; 1261 -8.8; 1387 -8.8; 1526 -8.9; 1678 -8.8; 1846 -9.0; 2031 -9.3; 2234 -9.8; 2457 -10.1; 2703 -9.7; 2973 -8.9; 3270 -7.9; 3597 -8.3; 3957 -11.2; 4353 -12.9; 4788 -12.5; 5267 -10.4; 5793 -7.1; 6373 -4.8; 7010 -5.5; 7711 -7.0; 8482 -7.6; 9330 -8.4; 10263 -10.2; 11289 -11.2; 12418 -10.0; 13660 -8.7; 15026 -9.7; 16529 -11.0; 18182 -9.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-W1000 Sovereign GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-W1000 Sovereign ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.28 | 6.1 dB  |
| Peaking | 233 Hz   | 1.09 | 5.9 dB  |
| Peaking | 1563 Hz  | 0.22 | -3.0 dB |
| Peaking | 11319 Hz | 3.64 | -4.0 dB |
| Peaking | 16915 Hz | 1.32 | -4.6 dB |
| Peaking | 509 Hz   | 3.71 | -1.4 dB |
| Peaking | 2264 Hz  | 0.15 | 0.5 dB  |
| Peaking | 4628 Hz  | 3.59 | -5.5 dB |
| Peaking | 6485 Hz  | 3.5  | 4.2 dB  |
| Peaking | 10830 Hz | 1.08 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.1 dB  |
| Peaking | 125 Hz   | 1.41 | 3.1 dB  |
| Peaking | 250 Hz   | 1.41 | 6.1 dB  |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | -3.9 dB |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -5.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-W1000%20Sovereign/Audio-Technica%20ATH-W1000%20Sovereign.png)