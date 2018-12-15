# Jaybird Run

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.7dB
GraphicEQ: 21 -1.2; 23 -1.2; 25 -1.3; 28 -1.3; 31 -1.3; 34 -1.3; 37 -1.3; 41 -1.3; 45 -1.3; 49 -1.3; 54 -1.4; 60 -1.7; 66 -2.1; 72 -2.3; 79 -2.6; 87 -3.0; 96 -3.3; 106 -3.7; 116 -4.0; 128 -4.4; 141 -4.8; 155 -5.3; 170 -5.5; 187 -5.6; 206 -5.3; 227 -5.0; 249 -4.5; 274 -4.0; 302 -3.6; 332 -3.1; 365 -2.6; 402 -2.1; 442 -1.5; 486 -0.9; 535 -0.2; 588 0.4; 647 1.0; 712 1.5; 783 1.6; 861 1.3; 947 0.5; 1042 -0.4; 1146 -1.2; 1261 -1.9; 1387 -2.1; 1526 -2.5; 1678 -3.0; 1846 -3.7; 2031 -4.4; 2234 -4.7; 2457 -4.6; 2703 -3.7; 2973 -2.3; 3270 -0.9; 3597 0.1; 3957 0.7; 4353 1.1; 4788 1.3; 5267 0.9; 5793 -0.8; 6373 -5.6; 7010 -9.8; 7711 -5.8; 8482 -2.3; 9330 -4.2; 10263 -5.1; 11289 -0.5; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird Run GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-17**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird Run ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 176 Hz   | 0.58 | -5.4 dB  |
| Peaking | 713 Hz   | 1.99 | 2.9 dB   |
| Peaking | 2103 Hz  | 1.86 | -4.9 dB  |
| Peaking | 7084 Hz  | 4.55 | -10.1 dB |
| Peaking | 22086 Hz | 2.26 | -2.1 dB  |
| Peaking | 25 Hz    | 1.27 | -1.1 dB  |
| Peaking | 2661 Hz  | 5.57 | -1.5 dB  |
| Peaking | 4023 Hz  | 3.03 | 1.6 dB   |
| Peaking | 5104 Hz  | 4.36 | 2.2 dB   |
| Peaking | 9944 Hz  | 6.09 | -5.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20Run/Jaybird%20Run.png)