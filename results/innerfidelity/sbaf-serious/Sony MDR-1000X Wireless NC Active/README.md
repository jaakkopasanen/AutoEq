# Sony MDR-1000X Wireless NC Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.6; 23 -8.3; 25 -8.0; 28 -7.6; 31 -7.3; 34 -7.1; 37 -6.9; 41 -6.8; 45 -6.7; 49 -6.7; 54 -6.8; 60 -6.9; 66 -7.1; 72 -7.4; 79 -7.7; 87 -8.1; 96 -8.5; 106 -8.8; 116 -8.9; 128 -9.2; 141 -9.2; 155 -9.2; 170 -8.8; 187 -8.5; 206 -8.0; 227 -7.3; 249 -7.0; 274 -7.3; 302 -7.0; 332 -6.1; 365 -5.0; 402 -4.7; 442 -5.3; 486 -5.7; 535 -5.6; 588 -3.7; 647 -4.3; 712 -6.3; 783 -3.6; 861 -3.2; 947 -3.4; 1042 -2.8; 1146 -0.5; 1261 -1.5; 1387 -2.3; 1526 -4.9; 1678 -6.8; 1846 -8.4; 2031 -8.3; 2234 -7.7; 2457 -5.1; 2703 -3.0; 2973 -4.7; 3270 -5.4; 3597 -5.5; 3957 -8.5; 4353 -10.2; 4788 -7.2; 5267 -7.8; 5793 -10.4; 6373 -8.5; 7010 -4.1; 7711 -6.1; 8482 -8.3; 9330 -8.2; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1000X Wireless NC Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1000X Wireless NC Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 1.64 | -2.3 dB  |
| Peaking | 136 Hz  | 1.07 | -3.2 dB  |
| Peaking | 1333 Hz | 0.84 | 15.2 dB  |
| Peaking | 1912 Hz | 0.7  | -15.7 dB |
| Peaking | 2706 Hz | 2.03 | 8.9 dB   |
| Peaking | 386 Hz  | 6.68 | 1.5 dB   |
| Peaking | 6052 Hz | 5.62 | -4.9 dB  |
| Peaking | 7011 Hz | 3.32 | 5.2 dB   |
| Peaking | 7523 Hz | 6.21 | -1.3 dB  |
| Peaking | 8769 Hz | 6.33 | -2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-1000X%20Wireless%20NC%20Active/Sony%20MDR-1000X%20Wireless%20NC%20Active.png)