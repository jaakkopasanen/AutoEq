# Beats Powerbeats 2 Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -4.2; 25 -4.6; 28 -5.0; 31 -5.4; 34 -5.8; 37 -6.1; 41 -6.4; 45 -6.7; 49 -7.0; 54 -7.5; 60 -8.2; 66 -8.9; 72 -9.5; 79 -10.1; 87 -10.8; 96 -11.5; 106 -12.2; 116 -12.9; 128 -13.5; 141 -14.2; 155 -14.8; 170 -15.1; 187 -15.4; 206 -15.5; 227 -15.4; 249 -15.1; 274 -14.6; 302 -14.1; 332 -13.4; 365 -12.6; 402 -11.6; 442 -10.3; 486 -8.7; 535 -6.7; 588 -4.8; 647 -2.8; 712 -1.0; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -0.5; 1261 -0.7; 1387 -0.8; 1526 -0.9; 1678 -1.6; 1846 -3.4; 2031 -5.2; 2234 -5.3; 2457 -4.7; 2703 -2.8; 2973 -0.8; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.5; 4788 -3.6; 5267 -5.6; 5793 -5.6; 6373 -6.4; 7010 -7.4; 7711 -7.9; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Powerbeats 2 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Powerbeats 2 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.34 | 3.3 dB  |
| Peaking | 204 Hz  | 0.52 | -9.7 dB |
| Peaking | 410 Hz  | 1.38 | -3.1 dB |
| Peaking | 837 Hz  | 0.72 | 9.0 dB  |
| Peaking | 3642 Hz | 2.41 | 6.0 dB  |
| Peaking | 1578 Hz | 2.44 | 3.4 dB  |
| Peaking | 2467 Hz | 0.98 | -4.0 dB |
| Peaking | 2911 Hz | 3.38 | 4.8 dB  |
| Peaking | 4354 Hz | 5.37 | 2.4 dB  |
| Peaking | 7445 Hz | 5.99 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | -9.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 8.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20Powerbeats%202%20Wireless/Beats%20Powerbeats%202%20Wireless.png)