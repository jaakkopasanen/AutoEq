# Bose QuietControl 30

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.7dB
GraphicEQ: 21 -3.5; 23 -3.6; 25 -3.7; 28 -3.7; 31 -3.6; 34 -3.4; 37 -3.2; 41 -2.9; 45 -2.6; 49 -2.3; 54 -2.1; 60 -2.1; 66 -2.2; 72 -2.2; 79 -2.4; 87 -2.6; 96 -2.7; 106 -2.9; 116 -3.0; 128 -3.0; 141 -3.0; 155 -2.9; 170 -2.7; 187 -2.4; 206 -2.1; 227 -1.8; 249 -1.6; 274 -1.5; 302 -1.4; 332 -1.4; 365 -1.4; 402 -1.2; 442 -0.7; 486 -0.0; 535 0.7; 588 1.1; 647 1.4; 712 1.5; 783 1.6; 861 1.1; 947 0.4; 1042 -0.2; 1146 -0.4; 1261 -0.5; 1387 -0.5; 1526 -0.9; 1678 -1.8; 1846 -2.9; 2031 -3.2; 2234 -2.0; 2457 -0.7; 2703 -0.3; 2973 -0.6; 3270 -0.9; 3597 -1.3; 3957 -2.3; 4353 -4.8; 4788 -4.0; 5267 -3.1; 5793 -1.5; 6373 -0.9; 7010 1.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -1.8; 11289 -0.0; 12418 0.0; 13660 0.0; 15026 -3.5; 16529 -2.8; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietControl 30 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-17**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietControl 30 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 25 Hz    |  0.7  | -3.6 dB |
| Peaking | 138 Hz   |  0.82 | -2.9 dB |
| Peaking | 1952 Hz  |  3.99 | -3.4 dB |
| Peaking | 4572 Hz  |  3.48 | -5.0 dB |
| Peaking | 15710 Hz |  4.37 | -4.8 dB |
| Peaking | 370 Hz   |  2.42 | -1.0 dB |
| Peaking | 683 Hz   |  2.14 | 2.1 dB  |
| Peaking | 5474 Hz  |  7.87 | -0.8 dB |
| Peaking | 7183 Hz  |  8.72 | 1.9 dB  |
| Peaking | 10287 Hz | 12.55 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20QuietControl%2030/Bose%20QuietControl%2030.png)