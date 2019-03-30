# Shure SRH1440
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.6; 60 -1.1; 66 -1.7; 72 -2.1; 79 -2.4; 87 -2.7; 96 -3.1; 106 -3.3; 116 -3.6; 128 -3.7; 141 -3.9; 155 -3.9; 170 -3.7; 187 -3.7; 206 -3.7; 227 -3.7; 249 -3.7; 274 -3.7; 302 -3.7; 332 -3.7; 365 -3.7; 402 -3.7; 442 -3.7; 486 -3.7; 535 -3.7; 588 -3.5; 647 -3.3; 712 -3.5; 783 -4.0; 861 -4.3; 947 -4.7; 1042 -5.1; 1146 -5.4; 1261 -5.8; 1387 -6.3; 1526 -6.8; 1678 -7.5; 1846 -8.2; 2031 -8.8; 2234 -9.1; 2457 -9.3; 2703 -9.6; 2973 -10.4; 3270 -11.5; 3597 -12.3; 3957 -12.5; 4353 -12.8; 4788 -12.9; 5267 -12.0; 5793 -9.4; 6373 -6.7; 7010 -6.4; 7711 -8.4; 8482 -10.9; 9330 -12.9; 10263 -13.9; 11289 -14.1; 12418 -13.3; 13660 -11.0; 15026 -8.0; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH1440 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1440 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.39 | 6.3 dB  |
| Peaking | 298 Hz   | 0.73 | 2.1 dB  |
| Peaking | 698 Hz   | 1.29 | 2.4 dB  |
| Peaking | 3836 Hz  | 1.29 | -6.3 dB |
| Peaking | 11273 Hz | 1.7  | -8.2 dB |
| Peaking | 2033 Hz  | 4.2  | -1.3 dB |
| Peaking | 5300 Hz  | 3.61 | -4.0 dB |
| Peaking | 6683 Hz  | 1.65 | 4.4 dB  |
| Peaking | 8686 Hz  | 2.85 | -3.2 dB |
| Peaking | 16302 Hz | 4.25 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.9 dB  |
| Peaking | 125 Hz   | 1.41 | 1.6 dB  |
| Peaking | 250 Hz   | 1.41 | 2.1 dB  |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | -5.5 dB |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Shure%20SRH1440/Shure%20SRH1440.png)