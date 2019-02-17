# Sony WF-SP700N
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -9.9; 25 -10.2; 28 -10.6; 31 -10.9; 34 -11.0; 37 -11.1; 41 -11.0; 45 -11.0; 49 -10.9; 54 -10.9; 60 -10.9; 66 -10.9; 72 -10.8; 79 -10.7; 87 -10.7; 96 -10.6; 106 -10.6; 116 -10.6; 128 -10.5; 141 -10.3; 155 -10.3; 170 -10.1; 187 -9.8; 206 -9.4; 227 -8.8; 249 -8.2; 274 -7.6; 302 -7.0; 332 -6.5; 365 -5.9; 402 -5.5; 442 -5.0; 486 -4.5; 535 -3.9; 588 -3.3; 647 -2.7; 712 -2.0; 783 -1.4; 861 -1.4; 947 -1.9; 1042 -3.0; 1146 -4.0; 1261 -4.7; 1387 -5.1; 1526 -5.4; 1678 -5.6; 1846 -5.8; 2031 -5.9; 2234 -5.2; 2457 -4.1; 2703 -3.5; 2973 -3.1; 3270 -3.0; 3597 -2.9; 3957 -2.6; 4353 -2.3; 4788 -1.1; 5267 -0.5; 5793 -1.8; 6373 -8.3; 7010 -5.9; 7711 -2.3; 8482 -2.5; 9330 -5.4; 10263 -11.8; 11289 -10.8; 12418 -5.9; 13660 -2.6; 15026 -2.6; 16529 -7.5; 18182 -12.2; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WF-SP700N GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WF-SP700N ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 41 Hz    | 0.29 | -8.3 dB  |
| Peaking | 187 Hz   | 0.84 | -4.2 dB  |
| Peaking | 1827 Hz  | 2.11 | -3.6 dB  |
| Peaking | 10692 Hz | 4.02 | -10.3 dB |
| Peaking | 18457 Hz | 1.47 | -10.8 dB |
| Peaking | 805 Hz   | 3.86 | 2.3 dB   |
| Peaking | 5417 Hz  | 3.42 | 3.5 dB   |
| Peaking | 6531 Hz  | 5.99 | -8.1 dB  |
| Peaking | 7917 Hz  | 3.65 | 2.5 dB   |
| Peaking | 22050 Hz | 1.64 | 0.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.3 dB |
| Peaking | 62 Hz    | 1.41 | -6.0 dB |
| Peaking | 125 Hz   | 1.41 | -6.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | -5.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WF-SP700N/Sony%20WF-SP700N.png)