# Plantronics BackBeat Go 600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.7dB
GraphicEQ: 21 -1.3; 23 -2.0; 25 -2.6; 28 -3.4; 31 -4.0; 34 -4.4; 37 -4.6; 41 -4.8; 45 -4.8; 49 -4.8; 54 -4.8; 60 -4.8; 66 -5.1; 72 -5.4; 79 -5.7; 87 -6.1; 96 -6.4; 106 -6.5; 116 -6.6; 128 -6.5; 141 -6.3; 155 -5.9; 170 -5.4; 187 -4.7; 206 -4.0; 227 -3.2; 249 -2.4; 274 -1.7; 302 -1.0; 332 -0.3; 365 0.8; 402 2.0; 442 2.6; 486 2.6; 535 2.2; 588 1.8; 647 1.4; 712 0.7; 783 0.1; 861 0.9; 947 0.8; 1042 0.1; 1146 1.2; 1261 1.6; 1387 0.9; 1526 -0.1; 1678 -1.0; 1846 -1.5; 2031 -1.2; 2234 -0.0; 2457 1.8; 2703 2.5; 2973 2.0; 3270 1.5; 3597 0.4; 3957 -1.6; 4353 -3.5; 4788 -2.0; 5267 0.6; 5793 1.3; 6373 -5.5; 7010 -6.4; 7711 -6.5; 8482 -9.0; 9330 -11.5; 10263 -11.7; 11289 -10.1; 12418 -6.7; 13660 -4.1; 15026 -3.5; 16529 -2.1; 18182 -0.2; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics BackBeat Go 600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-27**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics BackBeat Go 600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 36 Hz    | 1.19 | -3.0 dB  |
| Peaking | 122 Hz   | 0.57 | -6.6 dB  |
| Peaking | 459 Hz   | 1.12 | 3.9 dB   |
| Peaking | 10011 Hz | 1.49 | -12.6 dB |
| Peaking | 24000 Hz | 2.01 | -1.6 dB  |
| Peaking | 1979 Hz  | 2.49 | -4.8 dB  |
| Peaking | 2527 Hz  | 1.14 | 4.4 dB   |
| Peaking | 4350 Hz  | 4.2  | -4.2 dB  |
| Peaking | 5778 Hz  | 4.07 | 6.0 dB   |
| Peaking | 6549 Hz  | 5.03 | -5.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Plantronics%20BackBeat%20Go%20600/Plantronics%20BackBeat%20Go%20600.png)