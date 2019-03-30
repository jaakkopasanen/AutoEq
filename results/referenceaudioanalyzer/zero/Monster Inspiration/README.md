# Monster Inspiration
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -4.6; 25 -5.2; 28 -6.0; 31 -6.7; 34 -7.2; 37 -7.6; 41 -8.0; 45 -8.3; 49 -8.6; 54 -9.1; 60 -9.9; 66 -10.7; 72 -11.1; 79 -11.4; 87 -11.6; 96 -11.7; 106 -12.0; 116 -12.0; 128 -12.2; 141 -12.3; 155 -12.2; 170 -12.1; 187 -12.0; 206 -11.7; 227 -11.2; 249 -10.3; 274 -9.1; 302 -7.8; 332 -6.3; 365 -4.7; 402 -3.2; 442 -1.3; 486 -0.5; 535 -0.5; 588 -0.5; 647 -0.5; 712 -0.6; 783 -1.3; 861 -1.6; 947 -1.6; 1042 -1.6; 1146 -1.6; 1261 -1.6; 1387 -1.6; 1526 -1.6; 1678 -1.6; 1846 -2.1; 2031 -3.4; 2234 -5.2; 2457 -7.5; 2703 -9.6; 2973 -10.8; 3270 -11.3; 3597 -11.1; 3957 -10.4; 4353 -10.0; 4788 -10.7; 5267 -11.3; 5793 -9.9; 6373 -6.5; 7010 -4.6; 7711 -7.1; 8482 -10.0; 9330 -9.9; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Inspiration GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Inspiration ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 207 Hz  | 0.39 | -8.5 dB |
| Peaking | 498 Hz  | 0.78 | 10.6 dB |
| Peaking | 1868 Hz | 0.82 | 7.5 dB  |
| Peaking | 3008 Hz | 1.11 | -9.1 dB |
| Peaking | 5226 Hz | 5.5  | -3.4 dB |
| Peaking | 18 Hz   | 1.43 | 3.7 dB  |
| Peaking | 73 Hz   | 3.05 | -1.0 dB |
| Peaking | 5846 Hz | 5.09 | -1.9 dB |
| Peaking | 6739 Hz | 3.87 | 4.1 dB  |
| Peaking | 8671 Hz | 4.39 | -4.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB  |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | 6.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -6.2 dB |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Monster%20Inspiration/Monster%20Inspiration.png)