# E-Mu Teak Mahogany Cups

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.8dB
GraphicEQ: 21 -1.3; 23 -2.0; 25 -2.5; 28 -3.0; 31 -3.3; 34 -3.4; 37 -3.4; 41 -3.4; 45 -3.4; 49 -3.3; 54 -3.2; 60 -2.9; 66 -2.8; 72 -3.1; 79 -3.4; 87 -3.8; 96 -3.9; 106 -3.9; 116 -4.0; 128 -4.1; 141 -4.2; 155 -4.2; 170 -4.1; 187 -3.9; 206 -3.8; 227 -3.5; 249 -3.2; 274 -2.9; 302 -2.5; 332 -2.3; 365 -2.0; 402 -1.6; 442 -1.0; 486 -0.8; 535 -0.5; 588 0.2; 647 -0.1; 712 -0.5; 783 -0.6; 861 0.4; 947 -0.0; 1042 -0.2; 1146 -0.1; 1261 -0.1; 1387 -0.4; 1526 -0.6; 1678 -0.6; 1846 -0.3; 2031 0.4; 2234 1.0; 2457 2.0; 2703 2.5; 2973 2.7; 3270 2.0; 3597 2.0; 3957 2.2; 4353 1.3; 4788 0.5; 5267 0.1; 5793 0.7; 6373 1.5; 7010 2.3; 7711 0.3; 8482 0.0; 9330 -2.0; 10263 -1.9; 11289 -0.0; 12418 -0.2; 13660 -1.4; 15026 -0.1; 16529 0.0; 18182 0.0; 20000 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`E-Mu Teak Mahogany Cups GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-27**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `E-Mu Teak Mahogany Cups ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.89 | -2.8 dB |
| Peaking | 150 Hz   | 0.59 | -4.1 dB |
| Peaking | 3084 Hz  | 1.9  | 2.8 dB  |
| Peaking | 6799 Hz  | 6.76 | 2.5 dB  |
| Peaking | 9752 Hz  | 6.4  | -3.1 dB |
| Peaking | 588 Hz   | 5.11 | 0.9 dB  |
| Peaking | 1693 Hz  | 3.07 | -1.1 dB |
| Peaking | 3140 Hz  | 1.87 | 1.2 dB  |
| Peaking | 3223 Hz  | 5.03 | -1.8 dB |
| Peaking | 13585 Hz | 6.81 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/E-Mu%20Teak%20Mahogany%20Cups/E-Mu%20Teak%20Mahogany%20Cups.png)