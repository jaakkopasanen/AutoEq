# Sony MDR-XB80BS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.1; 25 -8.1; 28 -8.2; 31 -8.2; 34 -8.3; 37 -8.4; 41 -8.5; 45 -8.7; 49 -8.9; 54 -9.1; 60 -9.4; 66 -9.7; 72 -10.0; 79 -10.3; 87 -10.7; 96 -11.4; 106 -11.7; 116 -11.8; 128 -11.8; 141 -11.6; 155 -11.3; 170 -10.7; 187 -10.0; 206 -9.2; 227 -8.3; 249 -7.6; 274 -7.0; 302 -6.6; 332 -6.3; 365 -6.2; 402 -6.2; 442 -6.3; 486 -6.4; 535 -6.5; 588 -6.6; 647 -6.6; 712 -6.5; 783 -6.4; 861 -6.3; 947 -6.3; 1042 -6.4; 1146 -6.5; 1261 -6.4; 1387 -6.0; 1526 -5.4; 1678 -4.9; 1846 -4.5; 2031 -4.6; 2234 -5.2; 2457 -6.1; 2703 -6.3; 2973 -5.1; 3270 -3.4; 3597 -1.9; 3957 -0.8; 4353 -0.5; 4788 -1.2; 5267 -3.6; 5793 -7.5; 6373 -6.2; 7010 -4.0; 7711 -6.0; 8482 -7.2; 9330 -6.4; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB80BS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB80BS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.29 | -1.5 dB |
| Peaking | 100 Hz  | 0.96 | -1.6 dB |
| Peaking | 145 Hz  | 0.84 | -4.1 dB |
| Peaking | 296 Hz  | 1.18 | 1.6 dB  |
| Peaking | 4153 Hz | 2.48 | 6.4 dB  |
| Peaking | 1871 Hz | 3.09 | 1.8 dB  |
| Peaking | 2617 Hz | 6.91 | -1.3 dB |
| Peaking | 5087 Hz | 4.32 | 3.4 dB  |
| Peaking | 6055 Hz | 2.42 | -4.9 dB |
| Peaking | 6751 Hz | 5.95 | 4.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sony%20MDR-XB80BS/Sony%20MDR-XB80BS.png)