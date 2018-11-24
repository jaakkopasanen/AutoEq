# Sennheiser CXC-700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.7dB
GraphicEQ: 21 -0.7; 23 -1.1; 25 -1.4; 28 -1.8; 31 -2.0; 34 -2.2; 37 -2.4; 41 -2.5; 45 -2.6; 49 -2.6; 54 -2.8; 60 -3.1; 66 -3.4; 72 -3.7; 79 -3.9; 87 -4.3; 96 -4.6; 106 -5.0; 116 -5.4; 128 -5.7; 141 -5.9; 155 -6.0; 170 -5.9; 187 -5.8; 206 -5.5; 227 -5.1; 249 -4.6; 274 -4.2; 302 -3.9; 332 -3.4; 365 -2.8; 402 -2.1; 442 -1.4; 486 -0.8; 535 -0.0; 588 0.6; 647 1.3; 712 1.6; 783 1.5; 861 1.0; 947 0.3; 1042 -0.2; 1146 -0.7; 1261 -1.3; 1387 -1.6; 1526 -1.7; 1678 -1.9; 1846 -2.1; 2031 -2.1; 2234 -1.4; 2457 -0.4; 2703 0.2; 2973 0.4; 3270 0.3; 3597 0.1; 3957 -0.2; 4353 -1.0; 4788 -1.3; 5267 -2.0; 5793 -3.9; 6373 -5.9; 7010 -4.0; 7711 -1.6; 8482 -3.8; 9330 -7.6; 10263 -5.3; 11289 -0.1; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser CXC-700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-17**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CXC-700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 80 Hz    | 0.49 | -3.1 dB |
| Peaking | 186 Hz   | 0.96 | -4.5 dB |
| Peaking | 1772 Hz  | 3.08 | -2.2 dB |
| Peaking | 8388 Hz  | 1.26 | -5.0 dB |
| Peaking | 24000 Hz | 2.11 | -4.7 dB |
| Peaking | 710 Hz   | 3.1  | 2.5 dB  |
| Peaking | 6425 Hz  | 2.7  | -8.2 dB |
| Peaking | 7850 Hz  | 1.36 | 9.0 dB  |
| Peaking | 9535 Hz  | 2.95 | -9.7 dB |
| Peaking | 11231 Hz | 3.19 | 2.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sennheiser%20CXC-700/Sennheiser%20CXC-700.png)