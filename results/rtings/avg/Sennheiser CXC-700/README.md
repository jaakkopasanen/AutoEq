# Sennheiser CXC-700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.7dB
GraphicEQ: 21 -0.7; 23 -1.1; 25 -1.4; 28 -1.8; 31 -2.0; 34 -2.2; 37 -2.4; 41 -2.5; 45 -2.6; 49 -2.6; 54 -2.8; 60 -3.1; 66 -3.4; 72 -3.7; 79 -3.9; 87 -4.3; 96 -4.6; 106 -5.0; 116 -5.4; 128 -5.7; 141 -5.9; 155 -6.0; 170 -5.9; 187 -5.8; 206 -5.5; 227 -5.1; 249 -4.6; 274 -4.2; 302 -3.9; 332 -3.4; 365 -2.8; 402 -2.1; 442 -1.4; 486 -0.8; 535 -0.0; 588 0.6; 647 1.3; 712 1.6; 783 1.5; 861 1.0; 947 0.3; 1042 -0.2; 1146 -0.7; 1261 -1.3; 1387 -1.6; 1526 -1.7; 1678 -1.9; 1846 -2.1; 2031 -2.1; 2234 -1.4; 2457 -0.4; 2703 0.0; 2973 -0.0; 3270 -0.4; 3597 -0.9; 3957 -1.4; 4353 -2.3; 4788 -3.1; 5267 -4.6; 5793 -6.4; 6373 -7.1; 7010 -4.6; 7711 -2.1; 8482 -2.9; 9330 -5.0; 10263 -3.1; 11289 -0.1; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -2.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser CXC-700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-17**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CXC-700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 79 Hz    | 0.49 | -3.1 dB |
| Peaking | 186 Hz   | 0.96 | -4.5 dB |
| Peaking | 1764 Hz  | 3.08 | -2.1 dB |
| Peaking | 6231 Hz  | 1.8  | -6.6 dB |
| Peaking | 20329 Hz | 2.65 | -2.3 dB |
| Peaking | 338 Hz   | 2.94 | -1.1 dB |
| Peaking | 700 Hz   | 2.53 | 2.5 dB  |
| Peaking | 7762 Hz  | 5.67 | 2.6 dB  |
| Peaking | 9583 Hz  | 3.4  | -5.0 dB |
| Peaking | 11101 Hz | 2.09 | 2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20CXC-700/Sennheiser%20CXC-700.png)