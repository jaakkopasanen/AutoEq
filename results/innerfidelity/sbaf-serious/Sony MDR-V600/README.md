# Sony MDR-V600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -1.1; 45 -2.2; 49 -3.2; 54 -4.2; 60 -5.1; 66 -5.6; 72 -6.2; 79 -7.3; 87 -8.2; 96 -8.5; 106 -7.9; 116 -7.5; 128 -8.7; 141 -9.8; 155 -10.5; 170 -10.1; 187 -10.1; 206 -10.9; 227 -11.2; 249 -11.3; 274 -11.2; 302 -11.0; 332 -10.7; 365 -10.4; 402 -10.6; 442 -11.0; 486 -10.3; 535 -10.0; 588 -9.5; 647 -8.1; 712 -8.8; 783 -8.4; 861 -8.2; 947 -7.9; 1042 -7.0; 1146 -6.3; 1261 -5.4; 1387 -5.3; 1526 -6.0; 1678 -6.5; 1846 -5.9; 2031 -4.5; 2234 -3.0; 2457 -2.0; 2703 -0.9; 2973 -0.5; 3270 -0.8; 3597 -2.9; 3957 -3.4; 4353 -5.3; 4788 -3.6; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.7; 9330 -9.3; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-V600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.62 | 8.2 dB  |
| Peaking | 103 Hz  | 0.3  | -3.0 dB |
| Peaking | 342 Hz  | 0.64 | -3.2 dB |
| Peaking | 2862 Hz | 1.93 | 6.2 dB  |
| Peaking | 5797 Hz | 3.63 | 6.3 dB  |
| Peaking | 87 Hz   | 7.14 | -0.8 dB |
| Peaking | 925 Hz  | 2.44 | -1.0 dB |
| Peaking | 1350 Hz | 1.76 | 2.0 dB  |
| Peaking | 1678 Hz | 3.91 | -2.0 dB |
| Peaking | 9391 Hz | 5.89 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -3.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-V600/Sony%20MDR-V600.png)