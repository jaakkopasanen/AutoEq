# Creative SoundBlaster EVO Zx
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -4.3; 25 -6.1; 28 -8.3; 31 -10.2; 34 -11.7; 37 -12.9; 41 -14.1; 45 -15.0; 49 -15.6; 54 -15.9; 60 -15.6; 66 -15.0; 72 -14.2; 79 -13.4; 87 -13.0; 96 -12.9; 106 -13.0; 116 -13.2; 128 -13.3; 141 -13.3; 155 -13.3; 170 -13.3; 187 -13.2; 206 -13.0; 227 -12.7; 249 -12.2; 274 -11.7; 302 -11.4; 332 -11.2; 365 -10.6; 402 -9.9; 442 -9.2; 486 -8.6; 535 -8.2; 588 -7.7; 647 -7.3; 712 -7.1; 783 -7.0; 861 -6.9; 947 -7.1; 1042 -7.3; 1146 -7.1; 1261 -6.4; 1387 -5.1; 1526 -3.5; 1678 -2.0; 1846 -0.6; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.8; 3597 -3.0; 3957 -4.7; 4353 -4.6; 4788 -5.0; 5267 -5.3; 5793 -3.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative SoundBlaster EVO Zx GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative SoundBlaster EVO Zx ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.87 | 7.0 dB  |
| Peaking | 49 Hz   | 0.93 | -8.5 dB |
| Peaking | 188 Hz  | 0.55 | -6.0 dB |
| Peaking | 2410 Hz | 1.24 | 7.0 dB  |
| Peaking | 6353 Hz | 6.65 | 5.2 dB  |
| Peaking | 17 Hz   | 1.22 | 0.6 dB  |
| Peaking | 1155 Hz | 3.76 | -1.6 dB |
| Peaking | 1786 Hz | 3.48 | 2.1 dB  |
| Peaking | 2907 Hz | 1.3  | -2.1 dB |
| Peaking | 3174 Hz | 3.95 | 3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB |
| Peaking | 62 Hz    | 1.41 | -8.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -5.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -1.9 dB |
| Peaking | 2000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Creative%20SoundBlaster%20EVO%20Zx/Creative%20SoundBlaster%20EVO%20Zx.png)