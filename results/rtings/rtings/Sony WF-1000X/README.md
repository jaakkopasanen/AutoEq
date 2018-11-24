# Sony WF-1000X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.7dB
GraphicEQ: 21 0.0; 23 3.5; 25 3.5; 28 3.4; 31 3.4; 34 3.4; 37 3.4; 41 3.3; 45 3.2; 49 3.1; 54 2.8; 60 2.3; 66 1.8; 72 1.3; 79 0.8; 87 0.2; 96 -0.4; 106 -1.1; 116 -1.6; 128 -2.1; 141 -2.4; 155 -2.8; 170 -2.9; 187 -3.1; 206 -3.0; 227 -2.7; 249 -2.5; 274 -2.4; 302 -2.5; 332 -2.7; 365 -2.9; 402 -3.1; 442 -3.0; 486 -2.8; 535 -2.5; 588 -2.1; 647 -1.5; 712 -1.0; 783 -0.6; 861 -0.2; 947 0.4; 1042 -0.2; 1146 -0.6; 1261 -1.0; 1387 -1.3; 1526 1.2; 1678 0.3; 1846 -1.3; 2031 -2.2; 2234 -2.2; 2457 -1.7; 2703 -0.6; 2973 0.7; 3270 1.2; 3597 1.4; 3957 1.5; 4353 1.4; 4788 2.2; 5267 2.7; 5793 1.8; 6373 -0.4; 7010 1.1; 7711 0.3; 8482 0.0; 9330 -2.2; 10263 -8.5; 11289 -7.1; 12418 -0.9; 13660 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WF-1000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WF-1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 39 Hz    | 0.31 | 4.1 dB   |
| Peaking | 149 Hz   | 0.65 | -4.5 dB  |
| Peaking | 448 Hz   | 1.43 | -2.3 dB  |
| Peaking | 5038 Hz  | 2.22 | 2.7 dB   |
| Peaking | 10637 Hz | 4.75 | -10.2 dB |
| Peaking | 1006 Hz  | 1.96 | 2.6 dB   |
| Peaking | 1229 Hz  | 1.3  | -2.4 dB  |
| Peaking | 1581 Hz  | 6.55 | 3.7 dB   |
| Peaking | 2285 Hz  | 1.82 | -2.6 dB  |
| Peaking | 3118 Hz  | 2.3  | 2.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sony%20WF-1000X/Sony%20WF-1000X.png)