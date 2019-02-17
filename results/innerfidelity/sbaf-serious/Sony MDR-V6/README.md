# Sony MDR-V6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.4; 45 -2.1; 49 -2.6; 54 -3.2; 60 -3.9; 66 -4.0; 72 -3.7; 79 -3.9; 87 -4.5; 96 -4.9; 106 -5.1; 116 -5.2; 128 -5.2; 141 -5.2; 155 -5.1; 170 -4.9; 187 -4.6; 206 -4.5; 227 -5.1; 249 -6.3; 274 -6.0; 302 -5.6; 332 -5.8; 365 -6.4; 402 -7.2; 442 -7.4; 486 -7.5; 535 -7.7; 588 -7.4; 647 -7.3; 712 -7.1; 783 -6.9; 861 -6.8; 947 -6.4; 1042 -6.5; 1146 -6.7; 1261 -7.4; 1387 -7.5; 1526 -8.5; 1678 -9.1; 1846 -9.2; 2031 -9.2; 2234 -9.7; 2457 -9.7; 2703 -10.9; 2973 -11.6; 3270 -11.5; 3597 -10.7; 3957 -9.6; 4353 -11.9; 4788 -11.5; 5267 -6.8; 5793 -2.4; 6373 -2.6; 7010 -5.9; 7711 -7.7; 8482 -10.3; 9330 -13.6; 10263 -12.9; 11289 -6.8; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-V6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.2  | 6.6 dB  |
| Peaking | 2966 Hz  | 0.99 | -4.6 dB |
| Peaking | 4676 Hz  | 4.77 | -4.9 dB |
| Peaking | 5989 Hz  | 3.41 | 7.2 dB  |
| Peaking | 9554 Hz  | 3.78 | -8.2 dB |
| Peaking | 60 Hz    | 2.68 | -0.9 dB |
| Peaking | 201 Hz   | 3.32 | 1.5 dB  |
| Peaking | 519 Hz   | 2.47 | -1.3 dB |
| Peaking | 1024 Hz  | 4.22 | 0.8 dB  |
| Peaking | 11630 Hz | 6.76 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | 0.8 dB  |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | -3.2 dB |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-V6/Sony%20MDR-V6.png)