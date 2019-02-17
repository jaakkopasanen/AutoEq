# Sony MDR-1000X Wired Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -7.7; 25 -8.5; 28 -9.4; 31 -10.3; 34 -11.0; 37 -11.7; 41 -12.4; 45 -13.0; 49 -13.5; 54 -14.0; 60 -14.5; 66 -14.8; 72 -14.8; 79 -14.7; 87 -14.3; 96 -14.0; 106 -14.0; 116 -14.7; 128 -14.8; 141 -13.3; 155 -12.9; 170 -10.4; 187 -11.3; 206 -10.4; 227 -9.1; 249 -8.1; 274 -7.3; 302 -6.9; 332 -6.7; 365 -6.8; 402 -6.9; 442 -7.0; 486 -7.5; 535 -7.6; 588 -7.2; 647 -8.0; 712 -7.9; 783 -6.6; 861 -6.6; 947 -5.6; 1042 -4.1; 1146 -2.5; 1261 -1.3; 1387 -1.2; 1526 -2.3; 1678 -3.8; 1846 -4.5; 2031 -3.7; 2234 -1.7; 2457 -0.5; 2703 -2.3; 2973 -5.5; 3270 -7.7; 3597 -9.3; 3957 -11.9; 4353 -12.1; 4788 -9.1; 5267 -10.3; 5793 -7.5; 6373 -4.0; 7010 -2.9; 7711 -6.3; 8482 -9.3; 9330 -8.6; 10263 -5.0; 11289 -4.7; 12418 -4.7; 13660 -4.7; 15026 -4.7; 16529 -4.7; 18182 -4.7; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1000X Wired Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1000X Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 46 Hz   | 0.91 | -3.1 dB |
| Peaking | 98 Hz   | 0.47 | -9.0 dB |
| Peaking | 2533 Hz | 1.04 | 4.5 dB  |
| Peaking | 4043 Hz | 2    | -9.9 dB |
| Peaking | 8823 Hz | 6.36 | -5.3 dB |
| Peaking | 298 Hz  | 2.18 | 1.8 dB  |
| Peaking | 724 Hz  | 1.12 | -2.9 dB |
| Peaking | 1284 Hz | 2.18 | 4.0 dB  |
| Peaking | 1808 Hz | 5.01 | -3.0 dB |
| Peaking | 6770 Hz | 9.46 | 4.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -8.5 dB |
| Peaking | 125 Hz   | 1.41 | -8.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -6.5 dB |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-1000X%20Wired%20Passive/Sony%20MDR-1000X%20Wired%20Passive.png)