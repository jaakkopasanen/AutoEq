# Sennheiser Game One
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -0.9; 49 -1.3; 54 -1.8; 60 -2.4; 66 -2.9; 72 -3.4; 79 -3.9; 87 -4.5; 96 -5.2; 106 -5.7; 116 -6.2; 128 -6.6; 141 -7.0; 155 -7.2; 170 -7.3; 187 -7.3; 206 -7.2; 227 -7.2; 249 -7.2; 274 -7.2; 302 -7.1; 332 -7.1; 365 -7.0; 402 -7.1; 442 -7.2; 486 -7.3; 535 -7.2; 588 -7.1; 647 -6.9; 712 -6.4; 783 -6.2; 861 -6.1; 947 -6.2; 1042 -6.3; 1146 -6.2; 1261 -6.5; 1387 -6.5; 1526 -6.2; 1678 -6.5; 1846 -6.9; 2031 -7.9; 2234 -8.5; 2457 -8.1; 2703 -7.4; 2973 -6.6; 3270 -5.9; 3597 -4.9; 3957 -3.3; 4353 -4.5; 4788 -6.5; 5267 -5.1; 5793 -4.4; 6373 -5.0; 7010 -6.6; 7711 -7.4; 8482 -7.0; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.7; 20000 -9.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Game One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Game One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.32 | 6.8 dB  |
| Peaking | 127 Hz  | 0.56 | -3.3 dB |
| Peaking | 2301 Hz | 3.98 | -2.2 dB |
| Peaking | 3990 Hz | 5.47 | 3.5 dB  |
| Peaking | 5840 Hz | 6.41 | 2.3 dB  |
| Peaking | 562 Hz  | 1.62 | -1.5 dB |
| Peaking | 669 Hz  | 1    | 1.2 dB  |
| Peaking | 7868 Hz | 6.69 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 3.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20Game%20One/Sennheiser%20Game%20One.png)