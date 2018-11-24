# Plantronics BackBeat Go 600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 21 -0.9; 23 -1.6; 25 -2.3; 28 -3.3; 31 -4.0; 34 -4.5; 37 -4.7; 41 -5.0; 45 -5.1; 49 -5.1; 54 -5.1; 60 -5.1; 66 -5.2; 72 -5.4; 79 -5.5; 87 -5.7; 96 -5.9; 106 -6.1; 116 -6.1; 128 -6.0; 141 -5.7; 155 -5.3; 170 -4.8; 187 -4.1; 206 -3.4; 227 -2.7; 249 -1.9; 274 -1.0; 302 -0.1; 332 0.6; 365 1.8; 402 3.1; 442 3.7; 486 3.8; 535 3.4; 588 2.9; 647 2.4; 712 1.5; 783 0.6; 861 1.1; 947 0.8; 1042 0.2; 1146 1.4; 1261 1.8; 1387 0.9; 1526 -0.5; 1678 -1.4; 1846 -1.4; 2031 -0.8; 2234 0.4; 2457 2.3; 2703 3.1; 2973 3.1; 3270 3.4; 3597 2.6; 3957 -0.5; 4353 -3.5; 4788 -2.1; 5267 1.0; 5793 2.7; 6373 -3.0; 7010 -3.9; 7711 -5.4; 8482 -8.7; 9330 -10.0; 10263 -8.3; 11289 -5.6; 12418 -2.2; 13660 -0.3; 15026 -0.2; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics BackBeat Go 600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-39**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics BackBeat Go 600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 39 Hz    | 1.09 | -3.4 dB  |
| Peaking | 121 Hz   | 0.59 | -6.0 dB  |
| Peaking | 463 Hz   | 1.31 | 5.0 dB   |
| Peaking | 3025 Hz  | 3.41 | 4.2 dB   |
| Peaking | 9317 Hz  | 2.18 | -10.7 dB |
| Peaking | 1252 Hz  | 6.24 | 1.9 dB   |
| Peaking | 1758 Hz  | 4.5  | -2.2 dB  |
| Peaking | 4422 Hz  | 7.95 | -4.0 dB  |
| Peaking | 5660 Hz  | 8.63 | 4.8 dB   |
| Peaking | 13775 Hz | 4.76 | 1.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Plantronics%20BackBeat%20Go%20600/Plantronics%20BackBeat%20Go%20600.png)