# Beyerdynamic DX 160
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.5; 23 -15.5; 25 -15.5; 28 -15.5; 31 -15.5; 34 -15.5; 37 -15.5; 41 -15.4; 45 -15.3; 49 -15.2; 54 -15.1; 60 -14.9; 66 -14.7; 72 -14.6; 79 -14.3; 87 -14.1; 96 -13.8; 106 -13.5; 116 -13.2; 128 -12.8; 141 -12.4; 155 -12.0; 170 -11.5; 187 -11.1; 206 -10.5; 227 -9.9; 249 -9.3; 274 -8.7; 302 -8.2; 332 -8.0; 365 -7.7; 402 -7.2; 442 -6.8; 486 -6.2; 535 -5.7; 588 -5.3; 647 -4.9; 712 -4.5; 783 -4.3; 861 -4.1; 947 -4.0; 1042 -3.8; 1146 -4.0; 1261 -4.2; 1387 -4.5; 1526 -4.8; 1678 -5.1; 1846 -5.4; 2031 -5.4; 2234 -5.1; 2457 -4.5; 2703 -3.5; 2973 -2.4; 3270 -1.4; 3597 -0.6; 3957 -0.5; 4353 -0.7; 4788 -1.8; 5267 -3.5; 5793 -6.0; 6373 -8.4; 7010 -8.0; 7711 -5.7; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DX 160 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DX 160 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.16 | -9.6 dB |
| Peaking | 827 Hz   | 0.98 | 2.4 dB  |
| Peaking | 3995 Hz  | 1.61 | 6.0 dB  |
| Peaking | 6494 Hz  | 4.3  | -4.4 dB |
| Peaking | 10693 Hz | 2.34 | -0.2 dB |
| Peaking | 836 Hz   | 1.88 | -0.9 dB |
| Peaking | 1139 Hz  | 0.83 | 1.0 dB  |
| Peaking | 2077 Hz  | 1.37 | -1.5 dB |
| Peaking | 3131 Hz  | 1.54 | 1.1 dB  |
| Peaking | 3918 Hz  | 5.69 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.1 dB |
| Peaking | 62 Hz    | 1.41 | -6.6 dB  |
| Peaking | 125 Hz   | 1.41 | -5.7 dB  |
| Peaking | 250 Hz   | 1.41 | -2.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB   |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB  |
| Peaking | 16000 Hz | 1.41 | 0.2 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DX%20160/Beyerdynamic%20DX%20160.png)