# Sony MDR-1000X Wireless NC Off
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -7.5; 25 -7.7; 28 -7.9; 31 -8.1; 34 -8.2; 37 -8.3; 41 -8.5; 45 -8.7; 49 -8.8; 54 -8.8; 60 -8.8; 66 -8.5; 72 -8.1; 79 -7.9; 87 -7.7; 96 -8.7; 106 -9.9; 116 -10.6; 128 -10.7; 141 -9.3; 155 -8.5; 170 -6.6; 187 -7.7; 206 -6.4; 227 -5.4; 249 -5.1; 274 -5.6; 302 -5.6; 332 -5.0; 365 -4.0; 402 -3.6; 442 -4.3; 486 -4.7; 535 -4.8; 588 -2.8; 647 -3.6; 712 -5.4; 783 -2.9; 861 -3.4; 947 -3.5; 1042 -3.2; 1146 -0.9; 1261 -1.1; 1387 -0.5; 1526 -2.2; 1678 -3.9; 1846 -5.9; 2031 -6.5; 2234 -6.6; 2457 -4.4; 2703 -2.6; 2973 -4.4; 3270 -4.8; 3597 -4.5; 3957 -7.7; 4353 -9.3; 4788 -6.4; 5267 -7.1; 5793 -8.7; 6373 -7.1; 7010 -3.5; 7711 -5.3; 8482 -7.7; 9330 -7.8; 10263 -5.6; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -5.5; 16529 -5.5; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1000X Wireless NC Off GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1000X Wireless NC Off ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 44 Hz   | 0.77 | -3.3 dB |
| Peaking | 123 Hz  | 2.47 | -4.8 dB |
| Peaking | 1223 Hz | 1.74 | 4.6 dB  |
| Peaking | 4331 Hz | 5.95 | -4.1 dB |
| Peaking | 8963 Hz | 6.19 | -3.1 dB |
| Peaking | 440 Hz  | 1.43 | 1.3 dB  |
| Peaking | 1515 Hz | 3.75 | 2.0 dB  |
| Peaking | 2097 Hz | 1.91 | -5.3 dB |
| Peaking | 2599 Hz | 2.11 | 4.7 dB  |
| Peaking | 5776 Hz | 8.37 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | 0.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-1000X%20Wireless%20NC%20Off/Sony%20MDR-1000X%20Wireless%20NC%20Off.png)