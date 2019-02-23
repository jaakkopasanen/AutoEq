# Sennheiser MM 550-X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.6; 79 -1.5; 87 -2.6; 96 -3.2; 106 -3.6; 116 -3.8; 128 -3.9; 141 -3.8; 155 -3.6; 170 -3.4; 187 -3.5; 206 -3.5; 227 -3.3; 249 -3.3; 274 -3.4; 302 -3.3; 332 -3.5; 365 -3.8; 402 -4.2; 442 -4.6; 486 -5.3; 535 -6.2; 588 -7.0; 647 -7.8; 712 -8.7; 783 -9.5; 861 -9.6; 947 -9.3; 1042 -9.0; 1146 -8.6; 1261 -8.4; 1387 -8.6; 1526 -9.1; 1678 -10.1; 1846 -12.8; 2031 -16.2; 2234 -16.4; 2457 -13.1; 2703 -11.1; 2973 -9.1; 3270 -6.6; 3597 -3.2; 3957 -0.7; 4353 -0.5; 4788 -2.0; 5267 -1.2; 5793 -2.4; 6373 -6.2; 7010 -4.7; 7711 -7.4; 8482 -11.8; 9330 -10.8; 10263 -9.2; 11289 -13.1; 12418 -14.9; 13660 -10.4; 15026 -6.6; 16529 -7.0; 18182 -9.2; 20000 -8.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser MM 550-X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MM 550-X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 16 Hz    | 0.08 | 5.5 dB   |
| Peaking | 2237 Hz  | 1.47 | -11.0 dB |
| Peaking | 4257 Hz  | 1.41 | 8.8 dB   |
| Peaking | 11673 Hz | 1.46 | -7.6 dB  |
| Peaking | 20721 Hz | 0.71 | -5.2 dB  |
| Peaking | 120 Hz   | 2.35 | -1.9 dB  |
| Peaking | 350 Hz   | 1.21 | 1.9 dB   |
| Peaking | 797 Hz   | 1.86 | -3.1 dB  |
| Peaking | 1536 Hz  | 3.76 | 2.0 dB   |
| Peaking | 8599 Hz  | 9.37 | -4.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 5.0 dB  |
| Peaking | 125 Hz   | 1.41 | 1.0 dB  |
| Peaking | 250 Hz   | 1.41 | 3.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -9.9 dB |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | -3.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20MM%20550-X/Sennheiser%20MM%20550-X.png)