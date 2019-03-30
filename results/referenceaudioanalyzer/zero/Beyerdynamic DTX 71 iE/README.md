# Beyerdynamic DTX 71 iE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.5; 23 -11.7; 25 -11.9; 28 -12.0; 31 -12.1; 34 -12.2; 37 -12.2; 41 -12.1; 45 -12.1; 49 -12.2; 54 -12.1; 60 -12.0; 66 -11.8; 72 -11.8; 79 -11.7; 87 -11.5; 96 -11.3; 106 -11.1; 116 -10.9; 128 -10.6; 141 -10.3; 155 -10.0; 170 -9.7; 187 -9.3; 206 -8.9; 227 -8.5; 249 -8.2; 274 -8.3; 302 -8.0; 332 -7.9; 365 -7.6; 402 -7.3; 442 -7.2; 486 -7.0; 535 -7.0; 588 -6.7; 647 -6.6; 712 -6.7; 783 -7.0; 861 -7.0; 947 -7.3; 1042 -7.6; 1146 -8.0; 1261 -8.4; 1387 -8.8; 1526 -9.3; 1678 -9.6; 1846 -9.6; 2031 -8.9; 2234 -7.5; 2457 -5.8; 2703 -4.0; 2973 -2.4; 3270 -1.1; 3597 -0.5; 3957 -0.5; 4353 -1.3; 4788 -2.9; 5267 -5.1; 5793 -6.9; 6373 -7.2; 7010 -5.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DTX 71 iE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DTX 71 iE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 44 Hz   | 0.26 | -5.8 dB |
| Peaking | 1862 Hz | 1.32 | -5.5 dB |
| Peaking | 3664 Hz | 0.99 | 7.6 dB  |
| Peaking | 5806 Hz | 3.15 | -3.8 dB |
| Peaking | 9701 Hz | 1.57 | -0.8 dB |
| Peaking | 635 Hz  | 2.36 | 0.5 dB  |
| Peaking | 1196 Hz | 4.18 | -0.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.6 dB |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DTX%2071%20iE/Beyerdynamic%20DTX%2071%20iE.png)