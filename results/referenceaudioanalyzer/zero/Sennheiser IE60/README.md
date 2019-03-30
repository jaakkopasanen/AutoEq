# Sennheiser IE60
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -6.3; 25 -6.9; 28 -7.6; 31 -8.2; 34 -8.7; 37 -9.1; 41 -9.6; 45 -10.0; 49 -10.3; 54 -10.6; 60 -10.9; 66 -11.1; 72 -11.2; 79 -11.2; 87 -11.2; 96 -11.2; 106 -11.4; 116 -11.8; 128 -11.9; 141 -11.9; 155 -11.6; 170 -11.5; 187 -11.3; 206 -11.1; 227 -10.8; 249 -10.5; 274 -10.2; 302 -9.8; 332 -9.5; 365 -9.0; 402 -8.6; 442 -8.1; 486 -7.6; 535 -7.0; 588 -6.5; 647 -5.9; 712 -5.2; 783 -4.6; 861 -4.0; 947 -3.3; 1042 -2.8; 1146 -2.2; 1261 -1.6; 1387 -0.9; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -1.0; 2457 -1.5; 2703 -2.1; 2973 -3.0; 3270 -4.3; 3597 -5.4; 3957 -6.1; 4353 -6.5; 4788 -7.3; 5267 -10.4; 5793 -14.7; 6373 -15.1; 7010 -10.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE60 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 16 Hz   | 0.92 | 2.8 dB   |
| Peaking | 48 Hz   | 0.62 | -2.6 dB  |
| Peaking | 167 Hz  | 0.44 | -4.7 dB  |
| Peaking | 1673 Hz | 0.71 | 6.6 dB   |
| Peaking | 6045 Hz | 3.64 | -10.7 dB |
| Peaking | 2666 Hz | 3.28 | 0.6 dB   |
| Peaking | 3675 Hz | 3.66 | -1.0 dB  |
| Peaking | 6842 Hz | 8.32 | -3.4 dB  |
| Peaking | 7405 Hz | 3.73 | 2.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.7 dB |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20IE60/Sennheiser%20IE60.png)