# Sennheiser MM 550-X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.9; 116 -1.1; 128 -1.1; 141 -1.1; 155 -0.9; 170 -0.7; 187 -0.8; 206 -0.8; 227 -0.6; 249 -0.5; 274 -0.6; 302 -0.6; 332 -0.7; 365 -1.1; 402 -1.5; 442 -1.9; 486 -2.6; 535 -3.4; 588 -4.3; 647 -5.1; 712 -6.0; 783 -6.8; 861 -6.9; 947 -6.6; 1042 -6.3; 1146 -5.9; 1261 -5.7; 1387 -5.9; 1526 -6.3; 1678 -7.4; 1846 -10.1; 2031 -13.5; 2234 -13.7; 2457 -10.4; 2703 -8.4; 2973 -6.4; 3270 -3.9; 3597 -0.8; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.6; 6373 -3.5; 7010 -4.0; 7711 -6.2; 8482 -9.0; 9330 -8.1; 10263 -6.6; 11289 -10.4; 12418 -12.1; 13660 -7.7; 15026 -6.5; 16529 -6.5; 18182 -6.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser MM 550-X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MM 550-X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 0.16 | 6.1 dB  |
| Peaking | 321 Hz   | 1.08 | 3.8 dB  |
| Peaking | 2186 Hz  | 3.14 | -9.4 dB |
| Peaking | 4488 Hz  | 1.4  | 7.4 dB  |
| Peaking | 12077 Hz | 2.85 | -6.2 dB |
| Peaking | 821 Hz   | 3.82 | -1.7 dB |
| Peaking | 1399 Hz  | 3.45 | 1.1 dB  |
| Peaking | 5759 Hz  | 8.45 | 1.9 dB  |
| Peaking | 8720 Hz  | 5.22 | -3.8 dB |
| Peaking | 10211 Hz | 5.37 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.6 dB  |
| Peaking | 125 Hz   | 1.41 | 3.8 dB  |
| Peaking | 250 Hz   | 1.41 | 5.4 dB  |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.1 dB |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20MM%20550-X/Sennheiser%20MM%20550-X.png)