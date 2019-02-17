# Sony MDR-1000X Wired NC Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.2; 25 -7.2; 28 -7.3; 31 -7.3; 34 -7.4; 37 -7.4; 41 -7.6; 45 -7.7; 49 -7.8; 54 -7.9; 60 -8.0; 66 -8.0; 72 -8.2; 79 -8.4; 87 -8.6; 96 -8.9; 106 -9.0; 116 -9.1; 128 -9.2; 141 -9.2; 155 -9.1; 170 -8.7; 187 -8.7; 206 -8.4; 227 -8.1; 249 -7.7; 274 -7.2; 302 -6.8; 332 -6.3; 365 -5.8; 402 -5.5; 442 -5.2; 486 -5.2; 535 -4.9; 588 -4.4; 647 -5.0; 712 -5.5; 783 -4.9; 861 -4.2; 947 -3.4; 1042 -2.1; 1146 -0.5; 1261 -1.0; 1387 -1.7; 1526 -3.8; 1678 -6.6; 1846 -8.9; 2031 -9.1; 2234 -7.5; 2457 -4.8; 2703 -4.3; 2973 -5.3; 3270 -5.4; 3597 -5.0; 3957 -7.8; 4353 -9.0; 4788 -6.5; 5267 -8.1; 5793 -10.0; 6373 -8.5; 7010 -5.6; 7711 -6.6; 8482 -8.0; 9330 -7.5; 10263 -5.6; 11289 -4.1; 12418 -2.6; 13660 -2.6; 15026 -2.6; 16529 -2.6; 18182 -2.6; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1000X Wired NC Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1000X Wired NC Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.18 | -4.1 dB |
| Peaking | 166 Hz   | 0.49 | -5.2 dB |
| Peaking | 1957 Hz  | 4.73 | -6.4 dB |
| Peaking | 5878 Hz  | 0.87 | -6.0 dB |
| Peaking | 19992 Hz | 2.7  | -4.1 dB |
| Peaking | 735 Hz   | 3.39 | -1.7 dB |
| Peaking | 1198 Hz  | 3.97 | 3.6 dB  |
| Peaking | 7167 Hz  | 4.9  | 4.4 dB  |
| Peaking | 9071 Hz  | 1.15 | -3.9 dB |
| Peaking | 11703 Hz | 1.13 | 2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | -3.3 dB |
| Peaking | 8000 Hz  | 1.41 | -5.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-1000X%20Wired%20NC%20Active/Sony%20MDR-1000X%20Wired%20NC%20Active.png)