# Plantronics BackBeat Go 600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.7dB
GraphicEQ: 21 -1.3; 23 -2.0; 25 -2.6; 28 -3.4; 31 -4.0; 34 -4.4; 37 -4.6; 41 -4.8; 45 -4.8; 49 -4.8; 54 -4.8; 60 -4.8; 66 -5.1; 72 -5.4; 79 -5.7; 87 -6.1; 96 -6.4; 106 -6.5; 116 -6.6; 128 -6.5; 141 -6.3; 155 -5.9; 170 -5.4; 187 -4.7; 206 -4.0; 227 -3.2; 249 -2.4; 274 -1.7; 302 -1.0; 332 -0.3; 365 0.8; 402 2.0; 442 2.6; 486 2.6; 535 2.2; 588 1.8; 647 1.4; 712 0.7; 783 0.1; 861 0.9; 947 0.8; 1042 0.1; 1146 1.2; 1261 1.6; 1387 0.9; 1526 -0.1; 1678 -1.0; 1846 -1.5; 2031 -1.2; 2234 -0.0; 2457 1.8; 2703 2.3; 2973 1.5; 3270 0.8; 3597 -0.6; 3957 -2.9; 4353 -4.8; 4788 -3.7; 5267 -2.0; 5793 -1.2; 6373 -6.7; 7010 -7.3; 7711 -7.9; 8482 -9.7; 9330 -10.2; 10263 -10.0; 11289 -10.9; 12418 -9.9; 13660 -7.4; 15026 -6.1; 16529 -5.2; 18182 -4.3; 20000 -3.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics BackBeat Go 600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-27**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics BackBeat Go 600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 1.23 | -2.9 dB |
| Peaking | 123 Hz   | 0.56 | -6.7 dB |
| Peaking | 452 Hz   | 1.03 | 3.9 dB  |
| Peaking | 9984 Hz  | 0.97 | -9.3 dB |
| Peaking | 17470 Hz | 0.37 | -3.4 dB |
| Peaking | 1983 Hz  | 2.53 | -4.7 dB |
| Peaking | 2500 Hz  | 1.19 | 4.6 dB  |
| Peaking | 4325 Hz  | 3.72 | -4.3 dB |
| Peaking | 5837 Hz  | 4.5  | 4.6 dB  |
| Peaking | 6517 Hz  | 5.38 | -4.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Plantronics%20BackBeat%20Go%20600/Plantronics%20BackBeat%20Go%20600.png)