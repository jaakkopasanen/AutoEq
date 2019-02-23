# Sony MDR-XB1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.9; 25 -5.7; 28 -6.9; 31 -8.0; 34 -8.7; 37 -9.1; 41 -9.4; 45 -9.7; 49 -10.0; 54 -10.7; 60 -11.3; 66 -11.7; 72 -11.9; 79 -12.2; 87 -12.6; 96 -13.0; 106 -13.3; 116 -13.5; 128 -13.9; 141 -14.1; 155 -14.2; 170 -14.3; 187 -14.4; 206 -14.3; 227 -14.2; 249 -13.9; 274 -13.2; 302 -12.4; 332 -11.6; 365 -10.8; 402 -10.1; 442 -9.0; 486 -7.8; 535 -6.9; 588 -4.7; 647 -2.3; 712 -0.8; 783 -0.5; 861 -0.5; 947 -1.3; 1042 -4.4; 1146 -7.4; 1261 -7.4; 1387 -5.0; 1526 -2.2; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -3.6; 2457 -11.4; 2703 -10.1; 2973 -7.6; 3270 -6.4; 3597 -5.8; 3957 -6.0; 4353 -5.9; 4788 -1.8; 5267 -0.5; 5793 -1.9; 6373 -6.5; 7010 -4.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 65 Hz   | 1.08 | -2.1 dB |
| Peaking | 188 Hz  | 0.49 | -7.9 dB |
| Peaking | 752 Hz  | 2.09 | 8.6 dB  |
| Peaking | 1799 Hz | 4.4  | 7.1 dB  |
| Peaking | 5278 Hz | 4.96 | 6.9 dB  |
| Peaking | 21 Hz   | 2.99 | 3.3 dB  |
| Peaking | 1191 Hz | 1.76 | 3.3 dB  |
| Peaking | 1200 Hz | 4.47 | -6.6 dB |
| Peaking | 2159 Hz | 7.77 | 5.6 dB  |
| Peaking | 2506 Hz | 4.76 | -7.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.9 dB |
| Peaking | 250 Hz   | 1.41 | -7.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-XB1000/Sony%20MDR-XB1000.png)