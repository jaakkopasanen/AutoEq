# Beats Studio3 Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -3.9; 25 -4.4; 28 -5.1; 31 -5.7; 34 -6.3; 37 -6.8; 41 -7.3; 45 -7.8; 49 -8.2; 54 -8.9; 60 -9.7; 66 -10.3; 72 -10.5; 79 -10.5; 87 -10.3; 96 -10.0; 106 -9.6; 116 -9.2; 128 -9.0; 141 -9.1; 155 -9.3; 170 -9.7; 187 -10.0; 206 -10.3; 227 -10.6; 249 -11.1; 274 -11.4; 302 -11.6; 332 -12.0; 365 -12.1; 402 -11.3; 442 -10.0; 486 -8.4; 535 -6.7; 588 -5.5; 647 -5.0; 712 -5.7; 783 -5.9; 861 -6.3; 947 -6.7; 1042 -6.2; 1146 -5.8; 1261 -5.9; 1387 -5.7; 1526 -5.3; 1678 -5.1; 1846 -5.0; 2031 -4.8; 2234 -3.9; 2457 -3.1; 2703 -3.9; 2973 -6.9; 3270 -8.7; 3597 -8.6; 3957 -5.9; 4353 -2.9; 4788 -0.5; 5267 -1.6; 5793 -2.4; 6373 -4.3; 7010 -5.2; 7711 -6.2; 8482 -6.5; 9330 -6.8; 10263 -8.9; 11289 -11.2; 12418 -11.3; 13660 -8.3; 15026 -6.9; 16529 -6.7; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Studio3 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Studio3 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.37 | 4.5 dB  |
| Peaking | 67 Hz    | 0.54 | -5.0 dB |
| Peaking | 315 Hz   | 1.76 | -5.4 dB |
| Peaking | 5100 Hz  | 2.94 | 6.2 dB  |
| Peaking | 11868 Hz | 2.78 | -5.8 dB |
| Peaking | 417 Hz   | 4.46 | -1.8 dB |
| Peaking | 622 Hz   | 3.09 | 2.4 dB  |
| Peaking | 2844 Hz  | 1.43 | 5.0 dB  |
| Peaking | 3063 Hz  | 5.79 | -3.8 dB |
| Peaking | 3492 Hz  | 3.7  | -5.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20Studio3%20Wireless/Beats%20Studio3%20Wireless.png)