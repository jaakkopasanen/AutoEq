# Beyerdynamic DTX 350
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -0.9; 45 -1.3; 49 -1.9; 54 -2.7; 60 -3.7; 66 -4.3; 72 -4.4; 79 -4.4; 87 -4.8; 96 -5.6; 106 -6.7; 116 -7.7; 128 -8.5; 141 -8.6; 155 -8.2; 170 -7.7; 187 -6.6; 206 -5.6; 227 -5.3; 249 -5.3; 274 -4.9; 302 -4.4; 332 -4.4; 365 -4.4; 402 -4.3; 442 -4.4; 486 -4.4; 535 -4.5; 588 -4.7; 647 -5.0; 712 -5.3; 783 -5.5; 861 -5.7; 947 -5.9; 1042 -6.0; 1146 -6.0; 1261 -6.0; 1387 -6.0; 1526 -6.2; 1678 -6.5; 1846 -7.0; 2031 -7.7; 2234 -8.1; 2457 -8.3; 2703 -8.5; 2973 -8.6; 3270 -7.8; 3597 -7.2; 3957 -7.7; 4353 -10.1; 4788 -12.3; 5267 -12.8; 5793 -11.4; 6373 -8.4; 7010 -6.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DTX 350 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DTX 350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.55 | 6.3 dB  |
| Peaking | 139 Hz  | 1.77 | -3.9 dB |
| Peaking | 377 Hz  | 0.6  | 2.3 dB  |
| Peaking | 2543 Hz | 2.37 | -2.0 dB |
| Peaking | 5144 Hz | 3.47 | -7.0 dB |
| Peaking | 62 Hz   | 4.99 | -0.6 dB |
| Peaking | 3722 Hz | 9.08 | 0.7 dB  |
| Peaking | 5940 Hz | 6.55 | -1.4 dB |
| Peaking | 7185 Hz | 3.92 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | 1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | -3.7 dB |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DTX%20350/Beyerdynamic%20DTX%20350.png)